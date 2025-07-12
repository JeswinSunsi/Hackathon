import os
from datetime import datetime
from typing import List, Optional

import bcrypt
from bson import ObjectId
from fastapi import FastAPI, HTTPException, status
from pymongo import MongoClient
from pydantic import BaseModel, EmailStr

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "forum_db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
BCRYPT_ROUNDS = int(os.getenv("BCRYPT_ROUNDS", "12"))

app = FastAPI(title="Forum API", version="1.0.0")

try:
    client = MongoClient(MONGODB_URL)
    db = client[DATABASE_NAME]
    users_collection = db.users
    questions_collection = db.questions
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully")
except Exception as e:
    print(f"❌ Failed to connect to MongoDB: {e}")
    raise

class UserRegistration(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class AnswerData(BaseModel):
    username: str
    answer: str
    time: datetime
    likes: int = 0
    liked_by: List[str] = []

class QuestionCreation(BaseModel):
    title: str
    subject: str
    description: str
    username: str
    tags: List[str] = []

class QuestionResponse(BaseModel):
    id: str
    title: str
    subject: str
    description: str
    username: str
    time: datetime
    tags: List[str] = []
    likes: int = 0
    liked_by: List[str] = []
    answers: List[AnswerData] = []

class NewAnswer(BaseModel):
    username: str
    answer: str

class LikeAction(BaseModel):
    username: str

def hash_user_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_user_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def convert_question_for_response(question_doc: dict) -> dict:
    question_doc["id"] = str(question_doc["_id"])
    del question_doc["_id"]
    return question_doc

def find_user_by_email(email: str) -> Optional[dict]:
    return users_collection.find_one({"email": email})

def check_if_user_exists(email: str) -> bool:
    return find_user_by_email(email) is not None

@app.post("/users/register")
async def register_new_user(user_data: UserRegistration):
    if check_if_user_exists(user_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email address already exists"
        )
    
    hashed_password = hash_user_password(user_data.password)
    new_user = {
        "name": user_data.name,
        "email": user_data.email,
        "password": hashed_password,
        "created_at": datetime.now()
    }
    
    try:
        result = users_collection.insert_one(new_user)
        return {
            "message": "User registered successfully! You can now log in.",
            "user_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user account"
        )

@app.post("/users/login")
async def login_user(credentials: UserLogin):
    user = find_user_by_email(credentials.email)
    if not user:
        return {
            "success": False,
            "message": "Invalid email or password"
        }
    
    if verify_user_password(credentials.password, user["password"]):
        return {
            "success": True,
            "username": user["name"],
            "message": "Login successful"
        }
    else:
        return {
            "success": False,
            "message": "Invalid email or password"
        }

@app.post("/questions")
async def create_new_question(question_data: QuestionCreation):
    new_question = {
        "title": question_data.title,
        "subject": question_data.subject,
        "description": question_data.description,
        "username": question_data.username,
        "tags": question_data.tags,
        "time": datetime.now(),
        "likes": 0,
        "liked_by": [],
        "answers": []
    }
    
    try:
        result = questions_collection.insert_one(new_question)
        return {
            "message": "Question posted successfully!",
            "question_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create question"
        )

@app.get("/questions")
async def get_all_questions():
    try:
        questions = list(questions_collection.find().sort("likes", -1))
        
        simplified_questions = []
        for question in questions:
            top_answer_text = None
            top_answer_author = None
            
            if question.get("answers"):
                most_liked_answer = max(
                    question["answers"], 
                    key=lambda answer: answer.get("likes", 0)
                )
                top_answer_text = most_liked_answer["answer"]
                top_answer_author = most_liked_answer["username"]
            
            simplified_questions.append({
                "id": str(question["_id"]),
                "title": question["title"],
                "subject": question["subject"],
                "tags": question.get("tags", []),
                "top_answer": top_answer_text,
                "top_answer_username": top_answer_author,
                "likes": question["likes"]
            })
        
        return simplified_questions
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve questions"
        )

@app.get("/questions/{question_id}")
async def get_question_details(question_id: str):
    try:
        question = questions_collection.find_one({"_id": ObjectId(question_id)})
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found"
            )
        
        if question.get("answers"):
            question["answers"] = sorted(
                question["answers"], 
                key=lambda answer: answer.get("likes", 0), 
                reverse=True
            )
        
        return convert_question_for_response(question)
        
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid question ID format"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve question details"
        )

@app.post("/questions/{question_id}/answers")
async def add_answer_to_question(question_id: str, answer_data: NewAnswer):
    try:
        new_answer = {
            "username": answer_data.username,
            "answer": answer_data.answer,
            "time": datetime.now(),
            "likes": 0,
            "liked_by": []
        }
        
        result = questions_collection.update_one(
            {"_id": ObjectId(question_id)},
            {"$push": {"answers": new_answer}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found"
            )
        
        return {"message": "Answer added successfully!"}
        
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid question ID format"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add answer"
        )

@app.post("/questions/{question_id}/like")
async def like_question(question_id: str, like_data: LikeAction):
    try:
        question = questions_collection.find_one({"_id": ObjectId(question_id)})
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found"
            )
        
        if like_data.username in question.get("liked_by", []):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already liked this question"
            )
        
        questions_collection.update_one(
            {"_id": ObjectId(question_id)},
            {
                "$inc": {"likes": 1},
                "$push": {"liked_by": like_data.username}
            }
        )
        
        return {"message": "Question liked successfully!"}
        
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid question ID format"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to like question"
        )

@app.post("/questions/{question_id}/answers/{answer_index}/like")
async def like_answer(question_id: str, answer_index: int, like_data: LikeAction):
    try:
        question = questions_collection.find_one({"_id": ObjectId(question_id)})
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found"
            )
        
        answers = question.get("answers", [])
        if answer_index >= len(answers) or answer_index < 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Answer not found"
            )
        
        if like_data.username in answers[answer_index].get("liked_by", []):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already liked this answer"
            )
        
        questions_collection.update_one(
            {"_id": ObjectId(question_id)},
            {
                "$inc": {f"answers.{answer_index}.likes": 1},
                "$push": {f"answers.{answer_index}.liked_by": like_data.username}
            }
        )
        
        return {"message": "Answer liked successfully!"}
        
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid question ID format"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to like answer"
        )

@app.get("/")
async def health_check():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"🚀 Starting API on {host}:{port}")
    
    uvicorn.run(
        app, 
        host=host, 
        port=port,
        reload=os.getenv("ENVIRONMENT") == "development"
    )