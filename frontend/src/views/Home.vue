<template>
  <div class="forum-container">
    <header class="forum-header">
      <h1 class="forum-title" @click="$router.push('/')" style="cursor: pointer;">StackIt Forums</h1>
      <div class="user-menu">


        <span style="display: flex;">
          <div style="padding: 0.6rem 2rem; background-color: #2563EB; color: white; border-radius: 0.6rem; cursor: pointer; margin-right: 0.5rem;" @click="$router.push('/create')">Ask a question</div>
          <div class="user-avatar">
          <div class="user-avatar-name">J</div>
        </div>
        </span>
        
      </div>
    </header>

    <main class="forum-main">
      <div class="content-area">
        <div class="search-container">
          <div class="search-input-wrapper">
            <input type="text" placeholder="Search for a topic or a question" class="search-input" />
          </div>
        </div>

        <div class="filter-tabs">
          <button class="filter-tab active">
            Latest Questions
          </button>
          <button class="filter-tab">
            Trending Topics
          </button>
          <button class="filter-tab">
            Most Answered
          </button>
        </div>

        <div class="questions-list">
          <div class="question-item" style="cursor: pointer;" @click="$router.push('/question/1')">
            <div class="question-header">
              <div class="question-category design">Design</div>
              <button class="question-options">
              </button>
            </div>
            <h3 class="question-title">How can I start my career as a Product Designer?</h3>
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
              <button class="action-btn">
                Share
              </button>
              <button class="action-btn">
                Write answer
              </button>
              <button class="action-btn">
                Save
              </button>
              <div class="likes">
                <button class="like-btn">
                </button>
                <span class="like-count">255</span>
              </div>
            </div>
            <div class="top-answer">
              <div class="top-answer-label">
                Top Answer
              </div>
              <div class="answer-author">
                <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #6366F1;"
                  class="author-avatar"></div>
                <span class="author-name">Johan Pritchel</span>
                <span class="author-time">2 days ago</span>
              </div>
              <p class="answer-preview">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed diam nonummy nibh
                euismod tempor incididunt ut labore et dolore magna aliquam erat, sed diam voluptua. At vero eos et
                accusam et justo duo dolores et ea rebum. St.</p>
              <button class="read-more-btn">Read all answers</button>
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
              <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #6366F1;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Johan Pritchel</div>
                <div class="contributor-answers">64 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#2</span>
              <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #F59E0B;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Howard Hogan</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#3</span>
              <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #EF4444;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Mitchell Johnson</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot pink"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#4</span>
              <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #10B981;"
                class="contributor-avatar"></div>
              <div class="contributor-info">
                <div class="contributor-name">Mycroft Smith</div>
                <div class="contributor-answers">54 answers</div>
              </div>
              <div class="status-dot green"></div>
            </div>
            <div class="contributor-item">
              <span class="rank">#5</span>
              <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #8B5CF6;"
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

.external-link-btn {
  background: none;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  padding: 8px;
  cursor: pointer;
  color: #64748B;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.external-link-btn:hover {
  border-color: #CBD5E1;
  background: #F8FAFC;
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

.dropdown-arrow {
  color: #64748B;
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

.search-container {
  margin-bottom: 24px;
}

.search-input-wrapper {
  position: relative;
  max-width: 500px;
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #94A3B8;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 40px;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 14px;
  background: white;
  transition: border-color 0.2s;
}

.search-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.search-input::placeholder {
  color: #94A3B8;
}

.filter-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.filter-tab {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  padding: 12px 16px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  color: #64748B;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}

.filter-tab:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
}

.filter-tab.active {
  background: #2563EB;
  border-color: #2563EB;
  color: white;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.question-item {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.2s;
}

.question-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #CBD5E1;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
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

.question-category.casual {
  background: #FEF3C7;
  color: #D97706;
}

.question-options {
  background: none;
  border: none;
  color: #94A3B8;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.question-options:hover {
  background: #F1F5F9;
  color: #64748B;
}

.question-title {
  font-size: 18px;
  font-weight: 600;
  color: #0F172A;
  margin: 0 0 16px 0;
  line-height: 1.4;
}

.question-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.tag {
  background: #F1F5F9;
  color: #475569;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
}

.question-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #64748B;
  font-size: 14px;
  margin-bottom: 20px;
}

.separator {
  color: #CBD5E1;
}

.question-actions {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.action-btn {
  background: none;
  border: none;
  color: #64748B;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
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
  padding: 4px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
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

.top-answer {
  border-top: 1px solid #E2E8F0;
  padding-top: 20px;
}

.top-answer-label {
  color: #D97706;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.answer-author {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.author-avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
}

.author-name {
  font-weight: 600;
  color: #0F172A;
  font-size: 14px;
}

.author-time {
  color: #64748B;
  font-size: 14px;
}

.answer-preview {
  color: #475569;
  font-size: 14px;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.read-more-btn {
  background: #EBF8FF;
  border: 1px solid #BFDBFE;
  color: #2563EB;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  width: 100%;
  transition: all 0.2s;
}

.read-more-btn:hover {
  background: #DBEAFE;
  border-color: #93C5FD;
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
  height: 40px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  padding: 0 16px;
  gap: 12px;
  color: white;
  font-size: 14px;
  font-weight: 500;
  position: relative;
  overflow: hidden;
}

.poll-bar.blue {
  background: #3B82F6;
}

.poll-bar.orange {
  background: #F59E0B;
}

.poll-bar.green {
  background: #10B981;
}

.poll-percentage {
  min-width: 35px;
  font-weight: 600;
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

/* Responsive Design */
@media (max-width: 768px) {
  .forum-main {
    flex-direction: column;
    padding: 16px;
  }

  .sidebar {
    width: 100%;
    order: -1;
  }

  .filter-tabs {
    flex-wrap: wrap;
  }

  .question-actions {
    flex-wrap: wrap;
    gap: 12px;
  }

  .likes {
    margin-left: 0;
  }
}

@media (max-width: 480px) {
  .forum-header {
    padding: 12px 16px;
  }

  .forum-title {
    font-size: 20px;
  }

  .question-item {
    padding: 16px;
  }

  .question-title {
    font-size: 16px;
  }
  .search-input-wrapper {
    max-width: 100%;
  }
}
</style>