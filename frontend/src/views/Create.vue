<template>
  <div class="forum-container">
    <header class="forum-header">
      <h1 class="forum-title">StackIt Forums</h1>
      <div class="user-menu">
        <div class="user-avatar">
          <div class="user-avatar-name">J</div>
        </div>
      </div>
    </header>

    <main class="forum-main">
      <div class="content-area">
        <div class="add-question-container">
          <div class="form-header">
            <h1>Ask a Question</h1>
            <p>Share your question with the community and get helpful answers</p>
          </div>

          <form @submit.prevent="submitQuestion" class="question-form">
            <div class="form-group">
              <label for="title" class="form-label">Question Title</label>
              <input
                id="title"
                v-model="questionData.title"
                type="text"
                class="form-input"
                placeholder="What's your question? Be specific and clear..."
                required
              />
            </div>

            <div class="form-group">
              <label for="description" class="form-label">Question Description</label>
              <div class="editor-toolbar">
                <button type="button" @click="formatText('bold')" class="toolbar-btn">
                  <strong>B</strong>
                </button>
                <button type="button" @click="formatText('italic')" class="toolbar-btn">
                  <em>I</em>
                </button>
                <button type="button" @click="formatText('underline')" class="toolbar-btn">
                  <u>U</u>
                </button>
                <button type="button" @click="insertList" class="toolbar-btn">
                  • List
                </button>
              </div>
              <div
                ref="editor"
                class="rich-editor"
                contenteditable="true"
                @input="updateDescription"
                @paste="handlePaste"
                data-placeholder="Describe your question in detail. Include what you've tried, what you expect to happen, and what actually happens..."
              ></div>
            </div>

            <div class="form-group">
              <label for="subject" class="form-label">Subject</label>
              <input
                id="subject"
                v-model="questionData.subject"
                type="text"
                class="form-input"
                placeholder="e.g., Vue, JavaScript, CSS, etc."
                required
              />
            </div>

            <div class="form-group">
              <label for="tags" class="form-label">Tags</label>
              <input
                id="tags"
                v-model="tagsInput"
                type="text"
                class="form-input"
                placeholder="Enter tags separated by commas (e.g., vue3, javascript, frontend)"
                @input="updateTags"
              />
              <div v-if="questionData.tags.length > 0" class="tags-preview">
                <span
                  v-for="tag in questionData.tags"
                  :key="tag"
                  class="tag-chip"
                >
                  {{ tag }}
                  <button type="button" @click="removeTag(tag)" class="remove-tag">×</button>
                </span>
              </div>
            </div>

            <div class="form-actions">
              <button type="button" @click="cancelQuestion" class="btn btn-secondary">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary" :disabled="!isFormValid">
                Post Question
              </button>
            </div>
          </form>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-section">
          <h3 class="sidebar-title">Top Contributors</h3>
          <div class="contributors-list">
            <div class="contributor-item">
              <span class="rank">#1</span>
              <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #6366F1;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Johan Pritchel</div>
                <div class="contributor-answers">64 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#2</span>
              <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #F59E0B;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Howard Hogan</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#3</span>
              <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #EF4444;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Mitchell Johnson</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#4</span>
              <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #10B981;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Mycroft Smith</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#5</span>
              <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #8B5CF6;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Ricky Pointing</div>
                <div class="contributor-answers">53 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
          </div>
        </div>

        <div class="sidebar-section">
          <h3 class="sidebar-title">Top Questions</h3>
          <div class="top-questions-list">
            <div class="top-question-item">
              <span class="question-rank">#1</span>
              <div class="question-content">
                <div class="question-text">How can I start my career as a Product Designer?</div>
                <div class="question-answers">1255 answers</div>
              </div>
            </div>
            <div class="top-question-item">
              <span class="question-rank">#2</span>
              <div class="question-content">
                <div class="question-text">Guys please give me a suggestion for a book to read from!</div>
                <div class="question-answers">1905 answers</div>
              </div>
            </div>
            <div class="top-question-item">
              <span class="question-rank">#3</span>
              <div class="question-content">
                <div class="question-text">What is a common skill you just can't seem to master?</div>
                <div class="question-answers">942 answers</div>
              </div>
            </div>
            <div class="top-question-item">
              <span class="question-rank">#4</span>
              <div class="question-content">
                <div class="question-text">I am a software engineer looking to find a remote job with a company in the
                  USA. What is some advice for me?</div>
                <div class="question-answers">520 answers</div>
              </div>
            </div>
            <div class="top-question-item">
              <span class="question-rank">#5</span>
              <div class="question-content">
                <div class="question-text">What is a common skill you just can't seem to master?</div>
                <div class="question-answers">745 answers</div>
              </div>
            </div>
          </div>
        </div>
      </aside>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const questionData = ref({
  title: '',
  description: '',
  subject: '',
  tags: []
})

const tagsInput = ref('')
const editor = ref(null)

const isFormValid = computed(() => {
  return questionData.value.title.trim() !== '' && 
         questionData.value.subject.trim() !== '' && 
         questionData.value.description.trim() !== ''
})

const formatText = (command) => {
  document.execCommand(command, false, null)
}

const insertList = () => {
  document.execCommand('insertUnorderedList', false, null)
}

const updateDescription = () => {
  questionData.value.description = editor.value.innerHTML
}

const handlePaste = (e) => {
  e.preventDefault()
  const text = e.clipboardData.getData('text/plain')
  document.execCommand('insertText', false, text)
}

const updateTags = () => {
  const tags = tagsInput.value.split(',').map(tag => tag.trim()).filter(tag => tag.length > 0)
  questionData.value.tags = tags
}

const removeTag = (tagToRemove) => {
  questionData.value.tags = questionData.value.tags.filter(tag => tag !== tagToRemove)
  tagsInput.value = questionData.value.tags.join(', ')
}

const submitQuestion = () => {
  console.log('Question submitted:', questionData.value)
}

const cancelQuestion = () => {
  questionData.value = {
    title: '',
    description: '',
    subject: '',
    tags: []
  }
  tagsInput.value = ''
  if (editor.value) {
    editor.value.innerHTML = ''
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.forum-container {
  min-height: 100vh;
  background: #F8FAFC;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

.forum-header {
  background: white;
  border-bottom: 1px solid #E2E8F0;
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.forum-title {
  color: #2563EB;
  font-size: 24px;
  font-weight: 700;
  margin: 0;
}

.user-menu {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-avatar {
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
}

.user-avatar-name {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #FF6685;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: 600;
}

.forum-main {
  display: flex;
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.content-area {
  flex: 1;
}

.add-question-container {
  margin: 0 auto;
}

.form-header {
  border: 1px solid #E2E8F0;
  border-radius: 12px;    text-align: center;
  background-color: #fff;
  margin-bottom: 1rem;
  padding: 2rem 1rem;
}

.form-header h1 {
  color: #0F172A;
  font-size: 2.25rem;
  margin-bottom: 8px;
  font-weight: 700;
  letter-spacing: -0.025em;
}

.form-header p {
  color: #64748B;
  font-size: 1.125rem;
  font-weight: 400;
}

.question-form {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.form-group {
  margin-bottom: 24px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #0F172A;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.form-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.2s ease;
  box-sizing: border-box;
  background-color: white;
  color: #0F172A;
  font-family: inherit;
}

.form-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-input::placeholder {
  color: #94A3B8;
}

.editor-toolbar {
  display: flex;
  gap: 8px;
  margin-bottom: 0;
  padding: 12px 16px;
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-bottom: none;
  border-radius: 8px 8px 0 0;
}

.toolbar-btn {
  padding: 6px 12px;
  border: 1px solid #E2E8F0;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.2s;
  color: #64748B;
  font-weight: 500;
}

.toolbar-btn:hover {
  background: #F1F5F9;
  border-color: #CBD5E1;
  color: #475569;
}

.toolbar-btn:active {
  background: #E2E8F0;
  transform: translateY(1px);
}

.rich-editor {
  min-height: 150px;
  padding: 16px;
  border: 1px solid #E2E8F0;
  border-top: none;
  border-radius: 0 0 8px 8px;
  background: white;
  font-size: 1rem;
  line-height: 1.6;
  outline: none;
  overflow-y: auto;
  color: #0F172A;
  font-family: inherit;
}

.rich-editor:focus {
  border-color: #2563EB;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.rich-editor:empty::before {
  content: attr(data-placeholder);
  color: #94A3B8;
  pointer-events: none;
}

.tags-preview {
  margin-top: 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-chip {
  display: inline-flex;
  align-items: center;
  padding: 4px 8px;
  background: #F1F5F9;
  color: #475569;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 500;
  border: 1px solid #E2E8F0;
}

.remove-tag {
  background: none;
  border: none;
  color: #475569;
  margin-left: 6px;
  cursor: pointer;
  font-size: 1.25rem;
  line-height: 1;
  padding: 0;
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s;
}

.remove-tag:hover {
  background: #E2E8F0;
  color: #0F172A;
}

.form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid #E2E8F0;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  display: inline-block;
  font-family: inherit;
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: #2563EB;
  color: white;
  border: 1px solid #2563EB;
}

.btn-primary:hover:not(:disabled) {
  background: #1D4ED8;
  border-color: #1D4ED8;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.btn-primary:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2);
}

.btn-primary:disabled {
  background: #94A3B8;
  border-color: #94A3B8;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.btn-secondary {
  background: white;
  color: #64748B;
  border: 1px solid #E2E8F0;
}

.btn-secondary:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
  color: #475569;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.btn-secondary:active {
  transform: translateY(0);
  background: #F1F5F9;
}

.sidebar {
  width: 300px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.sidebar-section {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 24px;
}

.sidebar-title {
  font-size: 16px;
  font-weight: 700;
  color: #0F172A;
  margin: 0 0 20px 0;
}

.contributors-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.contributor-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
}

.rank {
  color: #64748B;
  font-size: 14px;
  font-weight: 600;
  min-width: 25px;
}

.contributor-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.contributor-info {
  flex: 1;
}

.contributor-name {
  font-weight: 600;
  color: #0F172A;
  font-size: 14px;
  margin-bottom: 2px;
}

.contributor-answers {
  color: #64748B;
  font-size: 12px;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-left: auto;
}

.status-dot.green {
  background: #10B981;
}

.status-dot.pink {
  background: #EC4899;
}

.top-questions-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.top-question-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.question-rank {
  color: #64748B;
  font-size: 14px;
  font-weight: 600;
  min-width: 25px;
  margin-top: 2px;
}

.question-content {
  flex: 1;
}

.question-text {
  color: #0F172A;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
  margin-bottom: 4px;
}

.question-answers {
  color: #64748B;
  font-size: 12px;
}

@media (max-width: 768px) {
  .forum-main {
    flex-direction: column;
    padding: 16px;
  }
  
  .sidebar {
    width: 100%;
    order: -1;
  }
  
  .question-form {
    padding: 24px;
  }
  
  .form-header h1 {
    font-size: 1.875rem;
  }
  
  .form-header p {
    font-size: 1rem;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .btn {
    width: 100%;
    justify-content: center;
  }
  
  .editor-toolbar {
    flex-wrap: wrap;
  }
}

@media (max-width: 480px) {
  .forum-header {
    padding: 12px 16px;
  }
  
  .forum-title {
    font-size: 20px;
  }
  
  .forum-main {
    padding: 12px;
  }
  
  .question-form {
    padding: 20px;
  }
  
  .form-header h1 {
    font-size: 1.5rem;
  }
}
</style>    