<template>
  <div class="landing-page">
    <header class="header">
      <div class="container">
        <div class="header-content">
          <router-link to="/" class="logo">StackIt Forums</router-link>
          <nav>
            <ul class="nav-links">
              <li><a href="#features" @click="scrollToSection('features')">Features</a></li>
              <li><a href="#topics" @click="scrollToSection('topics')">Topics</a></li>
              <li><a href="#about" @click="scrollToSection('about')">About</a></li>
              <li><a href="#contact" @click="scrollToSection('contact')">Contact</a></li>
            </ul>
          </nav>
          <div class="auth-buttons">
            <button class="btn btn-secondary" @click="handleSignIn">Sign In</button>
            <button class="btn btn-primary" @click="handleJoinNow">Join Now</button>
          </div>
        </div>
      </div>
    </header>
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <h1>Connect, Share, and Learn Together</h1>
          <p>Join thousands of passionate individuals sharing knowledge, asking questions, and building connections in our vibrant community.</p>
          <div class="hero-buttons">
            <button class="btn btn-primary btn-large" @click="handleGetStarted">Get Started Free</button>
            <button class="btn btn-secondary btn-large" @click="handleExploreTopics">Explore Topics</button>
          </div>
          <div class="stats-grid">
            <div class="stat-item" v-for="stat in stats" :key="stat.label">
              <span class="stat-number">{{ stat.number }}</span>
              <span class="stat-label">{{ stat.label }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="features" id="features">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Why Choose StackIt Forums?</h2>
          <p class="section-subtitle">Discover the features that make our community the best place to learn, share, and grow together.</p>
        </div>
        <div class="features-grid">
          <div class="feature-card" v-for="feature in features" :key="feature.title">
            <div class="feature-icon">{{ feature.icon }}</div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.description }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="popular-topics" id="topics">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Popular Topics</h2>
          <p class="section-subtitle">Explore the most active discussions and trending topics in our community.</p>
        </div>
        <div class="topics-grid">
          <a href="#" class="topic-card" v-for="topic in popularTopics" :key="topic.id" @click="handleTopicClick(topic)">
            <span class="topic-category" :class="topic.category.toLowerCase()">{{ topic.category }}</span>
            <h3 class="topic-title">{{ topic.title }}</h3>
            <div class="topic-stats">
              <span>{{ topic.likes }} likes</span>
              <span>{{ topic.answers }} answers</span>
            </div>
          </a>
        </div>
      </div>
    </section>
    <section class="cta">
      <div class="container">
        <h2>Ready to Join Our Community?</h2>
        <p>Start your journey today and become part of a thriving community of learners and experts.</p>
        <button class="btn btn-white btn-large" @click="handleCreateAccount">Create Your Account</button>
      </div>
    </section>
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section" v-for="section in footerSections" :key="section.title">
            <h3>{{ section.title }}</h3>
            <ul class="footer-links">
              <li v-for="link in section.links" :key="link.text">
                <a href="#" @click="handleFooterLinkClick(link)">{{ link.text }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2025 StackIt Forums. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {
      stats: [
        { number: '25,000+', label: 'Active Members' },
        { number: '150,000+', label: 'Questions Asked' },
        { number: '500,000+', label: 'Answers Provided' },
      ],
      features: [
        {
          icon: '💡',
          title: 'Expert Community',
          description: 'Connect with industry experts and experienced professionals who are ready to share their knowledge and help you succeed.'
        },
        {
          icon: '🚀',
          title: 'Fast Responses',
          description: 'Get quick answers to your questions with our active community that\'s online 24/7, ready to help when you need it most.'
        },
        {
          icon: '📚',
          title: 'Rich Content',
          description: 'Access a vast library of discussions, tutorials, and resources covering everything from beginner topics to advanced techniques.'
        },
        {
          icon: '🎯',
          title: 'Organized Topics',
          description: 'Find exactly what you\'re looking for with our well-organized categories and powerful search functionality.'
        },
        {
          icon: '🏆',
          title: 'Recognition System',
          description: 'Earn reputation points, badges, and recognition for your contributions to the community.'
        },
        {
          icon: '🔒',
          title: 'Safe & Secure',
          description: 'Enjoy a safe, moderated environment where respectful discussion and quality content are prioritized.'
        }
      ],
      popularTopics: [
        {
          id: 1,
          category: 'Design',
          title: 'How can I start my career as a Product Designer?',
          likes: 255,
          answers: 12
        },
        {
          id: 2,
          category: 'Technology',
          title: 'Best practices for React performance optimization',
          likes: 189,
          answers: 8
        },
        {
          id: 3,
          category: 'Career',
          title: 'Remote work tips for software engineers',
          likes: 342,
          answers: 15
        },
        {
          id: 4,
          category: 'General',
          title: 'What books changed your perspective on life?',
          likes: 156,
          answers: 23
        },
        {
          id: 5,
          category: 'Technology',
          title: 'Introduction to machine learning for beginners',
          likes: 278,
          answers: 11
        },
        {
          id: 6,
          category: 'Career',
          title: 'Negotiating salary as a junior developer',
          likes: 198,
          answers: 9
        }
      ],
      footerSections: [
        {
          title: 'StackIt Forums',
          links: [
            { text: 'About Us', action: 'about' },
            { text: 'Our Mission', action: 'mission' },
            { text: 'Team', action: 'team' },
            { text: 'Careers', action: 'careers' }
          ]
        },
        {
          title: 'Community',
          links: [
            { text: 'Guidelines', action: 'guidelines' },
            { text: 'Code of Conduct', action: 'conduct' },
            { text: 'Moderation', action: 'moderation' },
            { text: 'Help Center', action: 'help' }
          ]
        },
        {
          title: 'Resources',
          links: [
            { text: 'Documentation', action: 'docs' },
            { text: 'API', action: 'api' },
            { text: 'Blog', action: 'blog' },
            { text: 'Newsletter', action: 'newsletter' }
          ]
        },
        {
          title: 'Legal',
          links: [
            { text: 'Privacy Policy', action: 'privacy' },
            { text: 'Terms of Service', action: 'terms' },
            { text: 'Cookie Policy', action: 'cookies' },
            { text: 'GDPR', action: 'gdpr' }
          ]
        }
      ]
    }
  },
  methods: {
    handleSignIn() {
      // Handle sign in logic
      console.log('Sign in clicked');
      // this.$router.push('/signin');
    },
    handleJoinNow() {
      // Handle join now logic
      console.log('Join now clicked');
      // this.$router.push('/signup');
    },
    handleGetStarted() {
      // Handle get started logic
      console.log('Get started clicked');
      // this.$router.push('/signup');
    },
    handleExploreTopics() {
      // Handle explore topics logic
      console.log('Explore topics clicked');
      // this.$router.push('/topics');
    },
    handleCreateAccount() {
      // Handle create account logic
      console.log('Create account clicked');
      // this.$router.push('/signup');
    },
    handleTopicClick(topic) {
      // Handle topic click logic
      console.log('Topic clicked:', topic);
      // this.$router.push(`/topic/${topic.id}`);
    },
    handleFooterLinkClick(link) {
      // Handle footer link click logic
      console.log('Footer link clicked:', link);
      // this.$router.push(`/${link.action}`);
    },
    scrollToSection(sectionId) {
      const element = document.getElementById(sectionId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.landing-page {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: #0F172A;
  background: #F8FAFC;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Header */
.header {
  background: white;
  border-bottom: 1px solid #E2E8F0;
  padding: 16px 0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  color: #2563EB;
  font-size: 24px;
  font-weight: 700;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 32px;
  list-style: none;
}

.nav-links a {
  color: #64748B;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
  cursor: pointer;
}

.nav-links a:hover {
  color: #2563EB;
}

.auth-buttons {
  display: flex;
  gap: 12px;
}

.btn {
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
  font-size: 14px;
}

.btn-secondary {
  background: white;
  color: #64748B;
  border: 1px solid #E2E8F0;
}

.btn-secondary:hover {
  background: #F8FAFC;
  border-color: #CBD5E1;
}

.btn-primary {
  background: #2563EB;
  color: white;
}

.btn-primary:hover {
  background: #1D4ED8;
}

/* Hero Section */
.hero {
  padding: 80px 0;
  text-align: center;
  background: linear-gradient(135deg, #F8FAFC 0%, #EBF8FF 100%);
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 24px;
  color: #0F172A;
}

.hero p {
  font-size: 20px;
  color: #64748B;
  margin-bottom: 40px;
}

.hero-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-bottom: 60px;
}

.btn-large {
  padding: 16px 32px;
  font-size: 16px;
  font-weight: 600;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
  margin-top: 60px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 36px;
  font-weight: 700;
  color: #2563EB;
  display: block;
}

.stat-label {
  color: #64748B;
  font-size: 14px;
  font-weight: 500;
  margin-top: 8px;
}

/* Features Section */
.features {
  padding: 80px 0;
  background: white;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
}

.section-title {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
  color: #0F172A;
}

.section-subtitle {
  font-size: 18px;
  color: #64748B;
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 40px;
}

.feature-card {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 32px;
  text-align: center;
  transition: all 0.2s;
}

.feature-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #CBD5E1;
}

.feature-icon {
  width: 64px;
  height: 64px;
  background: #EBF8FF;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 24px;
  font-size: 24px;
  color: #2563EB;
}

.feature-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #0F172A;
}

.feature-description {
  color: #64748B;
  line-height: 1.6;
}

/* Popular Topics */
.popular-topics {
  padding: 80px 0;
  background: #F8FAFC;
}

.topics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.topic-card {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.2s;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.topic-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #CBD5E1;
}

.topic-category {
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: inline-block;
  margin-bottom: 16px;
}

.topic-category.design {
  background: #DBEAFE;
  color: #1D4ED8;
}

.topic-category.technology {
  background: #F3E8FF;
  color: #7C3AED;
}

.topic-category.career {
  background: #ECFDF5;
  color: #059669;
}

.topic-category.general {
  background: #FEF3C7;
  color: #D97706;
}

.topic-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #0F172A;
}

.topic-stats {
  display: flex;
  gap: 16px;
  color: #64748B;
  font-size: 14px;
}

/* CTA Section */
.cta {
  padding: 80px 0;
  background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
  color: white;
  text-align: center;
}

.cta h2 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
}

.cta p {
  font-size: 18px;
  margin-bottom: 32px;
  opacity: 0.9;
}

.btn-white {
  background: white;
  color: #2563EB;
}

.btn-white:hover {
  background: #F8FAFC;
}

/* Footer */
.footer {
  background: white;
  border-top: 1px solid #E2E8F0;
  padding: 40px 0;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
}

.footer-section h3 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #0F172A;
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 8px;
}

.footer-links a {
  color: #64748B;
  text-decoration: none;
  transition: color 0.2s;
  cursor: pointer;
}

.footer-links a:hover {
  color: #2563EB;
}

.footer-bottom {
  border-top: 1px solid #E2E8F0;
  padding-top: 24px;
  margin-top: 32px;
  text-align: center;
  color: #64748B;
  font-size: 14px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 0 16px;
  }

  .nav-links {
    display: none;
  }

  .hero h1 {
    font-size: 36px;
  }

  .hero p {
    font-size: 18px;
  }

  .hero-buttons {
    flex-direction: column;
    align-items: center;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .topics-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .hero {
    padding: 60px 0;
  }

  .hero h1 {
    font-size: 28px;
  }

  .section-title {
    font-size: 28px;
  }

  .cta h2 {
    font-size: 28px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>