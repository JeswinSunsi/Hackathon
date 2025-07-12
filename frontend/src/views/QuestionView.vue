<template>
  <div class="forum-container">
    <header class="forum-header">
      <h1 class="forum-title" @click="$router.push('/')" style="cursor: pointer;">StackIt Forums</h1>
      <div class="user-menu">
        <span style="display: flex;">
          <div style="padding: 0.6rem 2rem; background-color: #2563EB; color: white; border-radius: 0.6rem; margin-right: 0.5rem;">Ask a question</div>
          <div class="user-avatar">
          <div class="user-avatar-name">J</div>
        </div>
        </span>
      </div>
    </header>

    <main class="forum-main">
      <div class="content-area">
        <div class="breadcrumb">
          <span class="breadcrumb-link">Home</span>
          <span class="breadcrumb-separator">›</span>
          <span class="breadcrumb-current">Question</span>
        </div>

        <div class="question-detail">
          <div class="question-header">
            <div class="question-category design">Design</div>
            <button class="question-options">⋯</button>
          </div>
          
          <h1 class="question-title">How can I start my career as a Product Designer?</h1>
          
          <div class="question-tags">
            <span class="tag">#design</span>
            <span class="tag">#technology</span>
            <span class="tag">#career</span>
          </div>
          
          <div class="question-meta">
            <div class="question-author">
              <div class="author-avatar" style="background-color: #8B5CF6;"></div>
              <div class="author-info">
                <div class="author-name">Sarah Mitchell</div>
                <div class="author-time">Asked 2 days ago</div>
              </div>
            </div>
            <div class="question-stats">
              <span class="stat">255 likes</span>
              <span class="separator">•</span>
              <span class="stat">12 answers</span>
              <span class="separator">•</span>
              <span class="stat">1.2k views</span>
            </div>
          </div>
          
          <div class="question-content">
            <p>I'm currently working in marketing but I've always been passionate about design. I have some basic knowledge of design principles and I've been practicing with tools like Figma and Adobe Creative Suite in my free time.</p>
            <p>I'm looking for advice on how to transition into a product design role. What steps should I take? Should I build a portfolio first? Are there any specific courses or certifications that would be valuable?</p>
            <p>Any insights from experienced product designers would be greatly appreciated!</p>
          </div>
          
          <div class="question-actions">
            <button class="action-btn">Share</button>
            <button class="action-btn">Save</button>
            <button class="action-btn">Follow</button>
            <div class="likes">
              <button class="like-btn">♥</button>
              <span class="like-count">255</span>
            </div>
          </div>
        </div>

        <div class="answers-section">
          <div class="answers-header">
            <h2 class="answers-title">12 Answers</h2>
            <div class="sort-options">
              <button class="sort-btn active">Most Helpful</button>
              <button class="sort-btn">Newest</button>
              <button class="sort-btn">Oldest</button>
            </div>
          </div>

          <div class="answers-list">
            <div class="answer-item best-answer">
              <div class="answer-badge">Best Answer</div>
              <div class="answer-header">
                <div class="answer-author">
                  <div class="author-avatar" style="background-color: #6366F1;"></div>
                  <div class="author-info">
                    <div class="author-name">Johan Pritchel</div>
                    <div class="author-details">Senior Product Designer at Google • 2 days ago</div>
                  </div>
                </div>
                <div class="answer-votes">
                  <button class="vote-btn">▲</button>
                  <span class="vote-count">127</span>
                  <button class="vote-btn">▼</button>
                </div>
              </div>
              <div class="answer-content">
                <p>Great question! I made a similar transition from marketing to product design about 5 years ago. Here's what worked for me:</p>
                <p><strong>1. Build a strong portfolio</strong> - This is absolutely crucial. Start with redesigning existing products or creating concepts for apps you use daily. Focus on showing your process, not just the final designs.</p>
                <p><strong>2. Learn the fundamentals</strong> - Take courses on UX research, information architecture, and user psychology. I highly recommend "Design of Everyday Things" by Don Norman.</p>
                <p><strong>3. Network with designers</strong> - Join local design meetups, participate in design challenges, and connect with designers on LinkedIn. The design community is very supportive.</p>
                <p><strong>4. Consider a bootcamp or formal education</strong> - Programs like General Assembly or Springboard can provide structured learning and networking opportunities.</p>
                <p>Your marketing background is actually a huge advantage - you understand business goals and user needs, which many designers struggle with. Feel free to DM me if you have specific questions!</p>
              </div>
              <div class="answer-actions">
                <button class="action-btn">Reply</button>
                <button class="action-btn">Share</button>
                <button class="action-btn">Save</button>
              </div>
            </div>

            <div class="answer-item">
              <div class="answer-header">
                <div class="answer-author">
                  <div class="author-avatar" style="background-color: #F59E0B;"></div>
                  <div class="author-info">
                    <div class="author-name">Emily Chen</div>
                    <div class="author-details">UX Designer at Spotify • 1 day ago</div>
                  </div>
                </div>
                <div class="answer-votes">
                  <button class="vote-btn">▲</button>
                  <span class="vote-count">89</span>
                  <button class="vote-btn">▼</button>
                </div>
              </div>
              <div class="answer-content">
                <p>Adding to Johan's excellent advice - I'd also suggest:</p>
                <p><strong>Start with side projects</strong> - Look for non-profits or small businesses that need design help. This gives you real client experience and portfolio pieces.</p>
                <p><strong>Focus on user research</strong> - Many designers skip this, but understanding users is what separates good designers from great ones. Learn to conduct interviews and usability tests.</p>
                <p><strong>Stay updated</strong> - Follow design blogs, join design communities on Discord/Slack, and attend virtual conferences. The field moves fast!</p>
              </div>
              <div class="answer-actions">
                <button class="action-btn">Reply</button>
                <button class="action-btn">Share</button>
                <button class="action-btn">Save</button>
              </div>
            </div>

            <div class="answer-item">
              <div class="answer-header">
                <div class="answer-author">
                  <div class="author-avatar" style="background-color: #10B981;"></div>
                  <div class="author-info">
                    <div class="author-name">Marcus Rodriguez</div>
                    <div class="author-details">Lead Designer at Airbnb • 6 hours ago</div>
                  </div>
                </div>
                <div class="answer-votes">
                  <button class="vote-btn">▲</button>
                  <span class="vote-count">45</span>
                  <button class="vote-btn">▼</button>
                </div>
              </div>
              <div class="answer-content">
                <p>Your marketing background is actually a superpower in product design! You already understand user personas, conversion funnels, and business metrics.</p>
                <p>I'd recommend starting with conversion rate optimization projects - redesign landing pages or signup flows. This bridges your marketing knowledge with design skills and shows measurable impact.</p>
                <p>Also, consider getting familiar with design systems and component libraries. Most product teams use these extensively.</p>
              </div>
              <div class="answer-actions">
                <button class="action-btn">Reply</button>
                <button class="action-btn">Share</button>
                <button class="action-btn">Save</button>
              </div>
            </div>
          </div>

          <div class="write-answer">
            <h3 class="write-answer-title">Write an Answer</h3>
            <div class="answer-form">
              <textarea class="answer-input" placeholder="Share your knowledge and help others..."></textarea>
              <div class="form-actions">
                <button class="submit-btn">Submit Answer</button>
                <button class="cancel-btn">Cancel</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <aside class="sidebar">
        <div class="sidebar-section">
          <h3 class="sidebar-title">Top Contributors</h3>
          <div class="contributors-list">
            <div class="contributor-item">
              <span class="rank">#1</span>
              <div class="contributor-avatar" style="background-color: #6366F1;"></div>
              <div class="contributor-info">
                <div class="contributor-name">Johan Pritchel</div>
                <div class="contributor-answers">64 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#2</span>
              <div class="contributor-avatar" style="background-color: #F59E0B;"></div>
              <div class="contributor-info">
                <div class="contributor-name">Howard Hogan</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#3</span>
              <div class="contributor-avatar" style="background-color: #EF4444;"></div>
              <div class="contributor-info">
                <div class="contributor-name">Mitchell Johnson</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#4</span>
              <div class="contributor-avatar" style="background-color: #10B981;"></div>
              <div class="contributor-info">
                <div class="contributor-name">Mycroft Smith</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#5</span>
              <div class="contributor-avatar" style="background-color: #8B5CF6;"></div>
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
                <div class="question-text">I am a software engineer looking to find a remote job with a company in the USA. What is some advice for me?</div>
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
</script>

<style>
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

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 24px;
  font-size: 14px;
}

.breadcrumb-link {
  color: #2563EB;
  cursor: pointer;
}

.breadcrumb-link:hover {
  text-decoration: underline;
}

.breadcrumb-separator {
  color: #94A3B8;
}

.breadcrumb-current {
  color: #64748B;
}

.question-detail {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 32px;
  margin-bottom: 24px;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.question-category {
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.question-category.design {
  background: #DBEAFE;
  color: #1D4ED8;
}

.question-options {
  background: none;
  border: none;
  color: #94A3B8;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  font-size: 16px;
  transition: all 0.2s;
}

.question-options:hover {
  background: #F1F5F9;
  color: #64748B;
}

.question-title {
  font-size: 28px;
  font-weight: 700;
  color: #0F172A;
  margin: 0 0 20px 0;
  line-height: 1.3;
}

.question-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.tag {
  background: #F1F5F9;
  color: #475569;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
}

.question-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #E2E8F0;
}

.question-author {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-name {
  font-weight: 600;
  color: #0F172A;
  font-size: 14px;
}

.author-time {
  color: #64748B;
  font-size: 12px;
}

.question-stats {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #64748B;
}

.separator {
  color: #CBD5E1;
}

.question-content {
  line-height: 1.7;
  color: #374151;
  margin-bottom: 24px;
}

.question-content p {
  margin-bottom: 16px;
}

.question-content p:last-child {
  margin-bottom: 0;
}

.question-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}

.action-btn {
  background: none;
  border: none;
  color: #64748B;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 6px;
  transition: all 0.2s;
}

.action-btn:hover {
  background: #F1F5F9;
  color: #475569;
}

.likes {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 8px;
}

.like-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  border-radius: 4px;
  font-size: 16px;
  color: #EF4444;
  transition: all 0.2s;
}

.like-btn:hover {
  background: #FEF2F2;
}

.like-count {
  color: #EF4444;
  font-size: 14px;
  font-weight: 600;
}

.answers-section {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 32px;
}

.answers-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #E2E8F0;
}

.answers-title {
  font-size: 20px;
  font-weight: 700;
  color: #0F172A;
  margin: 0;
}

.sort-options {
  display: flex;
  gap: 8px;
}

.sort-btn {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 6px;
  padding: 8px 16px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 500;
  color: #64748B;
  transition: all 0.2s;
}

.sort-btn:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
}

.sort-btn.active {
  background: #2563EB;
  border-color: #2563EB;
  color: white;
}

.answers-list {
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin-bottom: 32px;
}

.answer-item {
  padding-bottom: 32px;
  border-bottom: 1px solid #E2E8F0;
}

.answer-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.best-answer {
  position: relative;
  background: #F0FDF4;
  padding: 24px;
  border-radius: 12px;
  border: 1px solid #BBF7D0;
}

.answer-badge {
  position: absolute;
  top: -8px;
  left: 24px;
  background: #10B981;
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.answer-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.answer-author {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-details {
  color: #64748B;
  font-size: 12px;
}

.answer-votes {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.vote-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  color: #64748B;
  transition: all 0.2s;
}

.vote-btn:hover {
  background: #F1F5F9;
  color: #475569;
}

.vote-count {
  font-weight: 600;
  color: #10B981;
  font-size: 14px;
}

.answer-content {
  line-height: 1.7;
  color: #374151;
  margin-bottom: 16px;
}

.answer-content p {
  margin-bottom: 16px;
}

.answer-content p:last-child {
  margin-bottom: 0;
}

.answer-actions {
  display: flex;
  gap: 16px;
}

.write-answer {
  border-top: 1px solid #E2E8F0;
  padding-top: 32px;
}

.write-answer-title {
  font-size: 18px;
  font-weight: 700;
  color: #0F172A;
  margin: 0 0 16px 0;
}

.answer-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.answer-input {
  width: 100%;
  min-height: 120px;
  padding: 16px;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 14px;
  font-family: inherit;
  line-height: 1.5;
  resize: vertical;
}

.answer-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.answer-input::placeholder {
  color: #94A3B8;
}

.form-actions {
  display: flex;
  gap: 12px;
}

.submit-btn {
  background: #2563EB;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.submit-btn:hover {
  background: #1D4ED8;
}

.cancel-btn {
  background: white;
  color: #64748B;
  border: 1px solid #E2E8F0;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.cancel-btn:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
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

  .question-detail {
    padding: 20px;
  }

  .answers-section {
    padding: 20px;
  }

  .question-title {
    font-size: 24px;
  }

  .question-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .sort-options {
    flex-wrap: wrap;
  }

  .answer-header {
    flex-direction: column;
    gap: 12px;
  }

  .answer-votes {
    flex-direction: row;
    align-self: flex-start;
  }
}

@media (max-width: 480px) {
  .forum-header {
    padding: 12px 16px;
  }

  .forum-title {
    font-size: 20px;
  }

  .question-title {
    font-size: 20px;
  }

  .question-actions {
    flex-wrap: wrap;
    gap: 12px;
  }

  .likes {
    margin-left: 0;
  }

  .form-actions {
    flex-direction: column;
  }

  .submit-btn,
  .cancel-btn {
    width: 100%;
  }
}
</style>