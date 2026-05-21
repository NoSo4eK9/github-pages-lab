// ==========================================
// CyberLab Interactive Features
// ==========================================

// Theme Toggle - Dark/Light Mode
class ThemeManager {
  constructor() {
    this.theme = localStorage.getItem('theme') || 'dark';
    this.init();
  }

  init() {
    this.applyTheme();
    this.createToggleButton();
  }

  createToggleButton() {
    const nav = document.querySelector('.nav-wrapper');
    if (!nav) return;

    const toggle = document.createElement('button');
    toggle.className = 'theme-toggle';
    toggle.setAttribute('aria-label', 'Toggle theme');
    toggle.innerHTML = '<span>🌙</span>';

    toggle.addEventListener('click', () => this.toggleTheme());
    nav.appendChild(toggle);
  }

  toggleTheme() {
    this.theme = this.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', this.theme);
    this.applyTheme();
  }

  applyTheme() {
    if (this.theme === 'light') {
      document.body.classList.add('light-mode');
      const toggle = document.querySelector('.theme-toggle span');
      if (toggle) toggle.textContent = '☀️';
    } else {
      document.body.classList.remove('light-mode');
      const toggle = document.querySelector('.theme-toggle span');
      if (toggle) toggle.textContent = '🌙';
    }
  }
}

// Counter Animation
class Counter {
  constructor(element, start, end, duration = 2000) {
    this.element = element;
    this.start = start;
    this.end = end;
    this.duration = duration;
    this.current = start;
    this.isVisible = false;
  }

  animate() {
    if (this.isVisible) return;

    this.isVisible = true;
    const range = this.end - this.start;
    const startTime = Date.now();

    const update = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / this.duration, 1);

      // Easing function for smooth animation
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      this.current = Math.floor(this.start + range * easeProgress);

      this.element.textContent = this.current;

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    };

    update();
  }

  check() {
    if (this.isVisible) return;

    const rect = this.element.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom > 0) {
      this.animate();
    }
  }
}

// Smooth Scroll Navigation
class SmoothScroll {
  constructor() {
    this.init();
  }

  init() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', (e) => this.handleClick(e));
    });
  }

  handleClick(e) {
    e.preventDefault();
    const target = document.querySelector(e.target.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}

// Page Transition Effects
class PageTransition {
  constructor() {
    this.init();
  }

  init() {
    document.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', (e) => this.handleLinkClick(e));
    });
  }

  handleLinkClick(e) {
    const href = e.target.getAttribute('href');
    
    // Skip external links and anchors
    if (!href || href.startsWith('http') || href.startsWith('#')) return;

    // For internal pages, add transition effect
    if (href.endsWith('.html')) {
      e.preventDefault();
      document.body.style.opacity = '0.7';
      setTimeout(() => {
        window.location.href = href;
      }, 300);
    }
  }
}

// Intersection Observer for animations
class AnimationObserver {
  constructor() {
    this.init();
  }

  init() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
          
          // Animate counters if they exist
          const counter = entry.target.querySelector('.stat-counter');
          if (counter && counter.textContent.match(/^\d+$/)) {
            const endValue = parseInt(counter.textContent);
            new Counter(counter, 0, endValue).animate();
          }
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .project-card, .timeline-item').forEach(el => {
      observer.observe(el);
    });
  }
}

// Keyboard Navigation
class KeyboardNav {
  constructor() {
    this.init();
  }

  init() {
    document.addEventListener('keydown', (e) => this.handleKeyDown(e));
  }

  handleKeyDown(e) {
    const nav = document.querySelectorAll('.nav a');
    const activeIndex = Array.from(nav).findIndex(a => a.classList.contains('active'));

    switch (e.key) {
      case 'ArrowRight':
        if (activeIndex < nav.length - 1) {
          nav[activeIndex + 1].click();
        }
        break;
      case 'ArrowLeft':
        if (activeIndex > 0) {
          nav[activeIndex - 1].click();
        }
        break;
    }
  }
}

// Form Validation
class FormValidator {
  static validate(form) {
    let isValid = true;

    form.querySelectorAll('input, textarea').forEach(field => {
      if (!field.value.trim()) {
        field.style.borderColor = 'var(--accent-3)';
        isValid = false;
      } else {
        field.style.borderColor = 'var(--accent)';
      }
    });

    return isValid;
  }

  static validateEmail(email) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
}

// Performance Monitor
class PerfMonitor {
  static log() {
    if (window.performance && window.performance.timing) {
      const timing = window.performance.timing;
      const loadTime = timing.loadEventEnd - timing.navigationStart;
      const domTime = timing.domContentLoadedEventEnd - timing.navigationStart;
      
      console.log(`
        🚀 Performance Metrics:
        ├─ DOM Ready: ${domTime}ms
        ├─ Page Load: ${loadTime}ms
        └─ Status: ${loadTime < 3000 ? '✅ Excellent' : '⚠️ Needs optimization'}
      `);
    }
  }
}

// Initialize all features when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  // Initialize features
  new ThemeManager();
  new SmoothScroll();
  new PageTransition();
  new AnimationObserver();
  new KeyboardNav();

  // Log performance metrics
  PerfMonitor.log();

  // Add keyboard shortcuts info
  console.log(`
    ⌨️  Keyboard Shortcuts:
    ├─ ← → : Navigate between pages
    ├─ Theme toggle button: Switch dark/light mode
    └─ Visit https://cyberlab.example.com for more info
  `);

  // Smooth page entrance
  document.body.style.opacity = '0';
  document.body.offsetHeight; // Force reflow
  document.body.style.transition = 'opacity 0.4s ease-out';
  document.body.style.opacity = '1';
});

// Utility functions
const Utils = {
  // Generate random color
  randomColor: () => {
    const colors = ['var(--accent)', 'var(--accent-2)', 'var(--accent-3)'];
    return colors[Math.floor(Math.random() * colors.length)];
  },

  // Debounce function for scroll events
  debounce: (func, wait) => {
    let timeout;
    return (...args) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  },

  // Get element by data attribute
  getByData: (attr, value) => {
    return document.querySelector(`[data-${attr}="${value}"]`);
  },

  // Format date
  formatDate: (date) => {
    return new Date(date).toLocaleDateString('uk-UA', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }
};

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    ThemeManager,
    Counter,
    SmoothScroll,
    PageTransition,
    AnimationObserver,
    KeyboardNav,
    FormValidator,
    PerfMonitor,
    Utils
  };
}

console.log('✨ CyberLab initialized successfully!');
