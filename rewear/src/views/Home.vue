<template>
  <div class="forum-container">
    <header class="forum-header">
      <h1 class="forum-title">Geek Forum</h1>
      <div class="user-menu">
        <button class="external-link-btn">↗</button>
        <div class="user-avatar">
          <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTYiIGN5PSIxNiIgcj0iMTYiIGZpbGw9IiNGRjY2ODUiLz4KPC9zdmc+" alt="User" />
        </div>
      </div>
    </header>

    <main class="forum-main">
      <div class="content-area">
        <div class="search-container">
          <input type="text" placeholder="Search for a topic or a question" class="search-input" />
        </div>

        <div class="filter-tabs">
          <button class="filter-tab active">📰 Latest Questions</button>
          <button class="filter-tab">🔥 Trending Topics</button>
          <button class="filter-tab">👤 Most Answered</button>
        </div>

        <div class="questions-list">
          <div class="question-item">
            <div class="question-category">Design</div>
            <div class="question-header">
              <h3 class="question-title">How can I start my career as a Product Designer?</h3>
              <div class="question-options">⋯</div>
            </div>
            <div class="question-tags">
              <span class="tag">#design</span>
              <span class="tag">#technology</span>
              <span class="tag">#career</span>
            </div>
            <div class="question-meta">
              <span class="time">2 days ago</span>
              <span class="separator">•</span>
              <span class="answers">12 answers</span>
            </div>
            <div class="question-actions">
              <button class="action-btn">🔗 Share</button>
              <button class="action-btn">✏️ Write answer</button>
              <button class="action-btn">💾 Save</button>
              <div class="likes">
                <span class="like-count">255</span>
                <button class="like-btn">❤️</button>
              </div>
            </div>
            <div class="top-answer">
              <span class="top-answer-label">👑 Top Answer</span>
              <div class="answer-author">
                <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTIiIGZpbGw9IiM2MzY2RjEiLz4KPC9zdmc+" alt="Johan Pritchel" class="author-avatar" />
                <span class="author-name">Johan Pritchel</span>
                <span class="author-time">2 days ago</span>
              </div>
              <p class="answer-preview">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed diam nonummy nibh euismod tempor incididunt ut labore et dolore magna aliquam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. St.</p>
              <button class="read-more-btn">Read all answers</button>
            </div>
          </div>

          <div class="question-item">
            <div class="question-category">Casual</div>
            <div class="question-header">
              <h3 class="question-title">Guys please give me a suggestion for a book to read from!</h3>
              <div class="question-options">⋯</div>
            </div>
            <div class="question-tags">
              <span class="tag">#design</span>
              <span class="tag">#technology</span>
              <span class="tag">#career</span>
            </div>
            <div class="question-meta">
              <span class="time">2 days ago</span>
              <span class="separator">•</span>
              <span class="answers">12 answers</span>
            </div>
            <div class="question-actions">
              <button class="action-btn">🔗 Share</button>
              <button class="action-btn">✏️ Write answer</button>
              <button class="action-btn">💾 Save</button>
            </div>
            <div class="poll-results">
              <div class="poll-option">
                <div class="poll-bar" style="width: 60%; background-color: #3B82F6;">
                  <span class="poll-percentage">60%</span>
                  <span class="poll-text">The Adventures of Sherlock Holmes</span>
                </div>
              </div>
              <div class="poll-option">
                <div class="poll-bar" style="width: 29%; background-color: #F59E0B;">
                  <span class="poll-percentage">29%</span>
                  <span class="poll-text">How can I start my career</span>
                </div>
              </div>
              <div class="poll-option">
                <div class="poll-bar" style="width: 12%; background-color: #10B981;">
                  <span class="poll-percentage">12%</span>
                  <span class="poll-text">How can I start my career</span>
                </div>
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
              <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTIiIGZpbGw9IiM2MzY2RjEiLz4KPC9zdmc+" alt="Johan Pritchel" class="contributor-avatar" />
              <div class="contributor-info">
                <div class="contributor-name">Johan Pritchel</div>
                <div class="contributor-answers">64 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#2</span>
              <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTIiIGZpbGw9IiNGNTlFMEIiLz4KPC9zdmc+" alt="Howard Hogan" class="contributor-avatar" />
              <div class="contributor-info">
                <div class="contributor-name">Howard Hogan</div>
                <div class="contributor-answers">24 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#3</span>
              <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTIiIGZpbGw9IiNFRjQ0NDQiLz4KPC9zdmc+" alt="Mitchell Johnson" class="contributor-avatar" />
              <div class="contributor-info">
                <div class="contributor-name">Mitchell Johnson</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#4</span>
              <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTIiIGZpbGw9IiMxMEI5ODEiLz4KPC9zdmc+" alt="Mycroft Smith" class="contributor-avatar" />
              <div class="contributor-info">
                <div class="contributor-name">Mycroft Smith</div>
                <div class="contributor-answers">48 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#5</span>
              <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTIiIGZpbGw9IiM4QjVDRjYiLz4KPC9zdmc+" alt="Ricky Pointing" class="contributor-avatar" />
              <div class="contributor-info">
                <div class="contributor-name">Ricky Pointing</div>
                <div class="contributor-answers">72 answers</div>
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
                <div class="question-answers">242 answers</div>
              </div>
            </div>
            <div class="top-question-item">
              <span class="question-rank">#4</span>
              <div class="question-content">
                <div class="question-text">I am a software engineer looking to find a remote job with a company in the USA. What is some advice for me?</div>
                <div class="question-answers">620 answers</div>
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

<script>
export default {
  name: 'GeekForum'
}
</script>

<style scoped>
.forum-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.forum-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.forum-title {
  color: #3B82F6;
  font-size: 24px;
  font-weight: 600;
  margin: 0;
}

.user-menu {
  display: flex;
  align-items: center;
  gap: 10px;
}

.external-link-btn {
  background: none;
  border: 1px solid #E5E7EB;
  border-radius: 6px;
  padding: 8px;
  cursor: pointer;
  color: #6B7280;
}

.user-avatar img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.forum-main {
  display: flex;
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.content-area {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.search-container {
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  font-size: 14px;
  background: #F9FAFB;
}

.filter-tabs {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
  border-bottom: 1px solid #E5E7EB;
}

.filter-tab {
  background: none;
  border: none;
  padding: 12px 0;
  cursor: pointer;
  font-size: 14px;
  color: #6B7280;
  border-bottom: 2px solid transparent;
}

.filter-tab.active {
  color: #3B82F6;
  border-bottom-color: #3B82F6;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.question-item {
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  padding: 20px;
  background: white;
}

.question-category {
  display: inline-block;
  background: #F3F4F6;
  color: #6B7280;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 8px;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.question-title {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin: 0;
  flex: 1;
}

.question-options {
  color: #9CA3AF;
  cursor: pointer;
  font-weight: bold;
}

.question-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.tag {
  background: #F3F4F6;
  color: #6B7280;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
}

.question-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #6B7280;
  font-size: 12px;
  margin-bottom: 16px;
}

.separator {
  color: #D1D5DB;
}

.question-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 16px;
}

.action-btn {
  background: none;
  border: none;
  color: #6B7280;
  cursor: pointer;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.likes {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 4px;
}

.like-count {
  color: #EF4444;
  font-size: 12px;
}

.like-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 12px;
}

.top-answer {
  border-top: 1px solid #E5E7EB;
  padding-top: 16px;
}

.top-answer-label {
  color: #F59E0B;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 8px;
  display: block;
}

.answer-author {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.author-avatar {
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.author-name {
  font-weight: 500;
  color: #111827;
  font-size: 12px;
}

.author-time {
  color: #6B7280;
  font-size: 12px;
}

.answer-preview {
  color: #6B7280;
  font-size: 14px;
  line-height: 1.4;
  margin: 8px 0;
}

.read-more-btn {
  background: #EBF8FF;
  border: none;
  color: #3B82F6;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  width: 100%;
}

.poll-results {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.poll-option {
  position: relative;
}

.poll-bar {
  height: 32px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  padding: 0 12px;
  gap: 8px;
  color: white;
  font-size: 12px;
  font-weight: 500;
}

.poll-percentage {
  min-width: 30px;
}

.sidebar {
  width: 280px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.sidebar-section {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.sidebar-title {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
  margin: 0 0 16px 0;
}

.contributors-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.contributor-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.rank {
  color: #6B7280;
  font-size: 12px;
  font-weight: 500;
  min-width: 20px;
}

.contributor-avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
}

.contributor-info {
  flex: 1;
}

.contributor-name {
  font-size: 12px;
  font-weight: 500;
  color: #111827;
}

.contributor-answers {
  font-size: 10px;
  color: #6B7280;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-dot.green {
  background: #10B981;
}

.status-dot.pink {
  background: #EF4444;
}

.top-questions-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.top-question-item {
  display: flex;
  gap: 8px;
  align-items: flex-start;
}

.question-rank {
  color: #6B7280;
  font-size: 12px;
  font-weight: 500;
  min-width: 20px;
}

.question-content {
  flex: 1;
}

.question-text {
  font-size: 12px;
  color: #111827;
  line-height: 1.4;
  margin-bottom: 2px;
}

.question-answers {
  font-size: 10px;
  color: #6B7280;
}
</style>