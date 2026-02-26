// ================================
// GOSMART - Main JavaScript
// ================================

// Language management
let currentLang = document.cookie.match(/lang=([^;]+)/)?.[1] || 'fr';

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    setLanguage(currentLang);
    setupLanguageSwitcher();
    setupContactForm();
    setupNavbar();
    setupMobileNav();
    setupVideoPlayer();
});

// ================================
// Language Functions
// ================================

function setLanguage(lang) {
    currentLang = lang;
    document.documentElement.lang = lang;
    document.cookie = `lang=${lang}; path=/; max-age=31536000`; // 1 year
    
    // Update all elements with data-fr and data-en attributes
    document.querySelectorAll('[data-fr]').forEach(element => {
        const text = element.getAttribute(`data-${lang}`);
        if (text) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                // Check for specific placeholder attributes
                const placeholder = element.getAttribute(`data-${lang}-placeholder`);
                if (placeholder) {
                    element.placeholder = placeholder;
                }
            } else if (element.tagName === 'OPTION') {
                element.textContent = text;
            } else {
                element.textContent = text;
            }
        }
    });
    
    // Update title
    const titleElement = document.querySelector('title');
    if (titleElement) {
        const title = titleElement.getAttribute(`data-${lang}`);
        if (title) {
            titleElement.textContent = title;
        }
    }
    
    // Update meta description
    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription) {
        const description = metaDescription.getAttribute(`data-${lang}`);
        if (description) {
            metaDescription.setAttribute('content', description);
        }
    }
    
    // Update placeholders
    document.querySelectorAll('[data-fr-placeholder]').forEach(element => {
        const placeholder = element.getAttribute(`data-${lang}-placeholder`);
        if (placeholder) {
            element.placeholder = placeholder;
        }
    });
    
    // Update active language button
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-lang') === lang) {
            btn.classList.add('active');
        }
    });
}

function setupLanguageSwitcher() {
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const lang = this.getAttribute('data-lang');
            setLanguage(lang);
        });
    });
}

// ================================
// Navigation Functions
// ================================

function setupNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    
    // Only add scroll effect on pages without .scrolled class
    if (!navbar.classList.contains('scrolled')) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
}

function setupMobileNav() {
    const toggle = document.getElementById('mobile-toggle');
    const mobileNav = document.getElementById('mobile-nav');
    
    if (!toggle || !mobileNav) return;
    
    toggle.addEventListener('click', () => {
        mobileNav.classList.toggle('active');
        toggle.classList.toggle('active');
    });
    
    // Close mobile nav when clicking a link
    mobileNav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileNav.classList.remove('active');
            toggle.classList.remove('active');
        });
    });
}

// ================================
// Contact Form
// ================================

function setupContactForm() {
    const form = document.getElementById('contact-form');
    const messageDiv = document.getElementById('form-message');
    
    if (!form) return;
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        formData.append('language', currentLang);
        
        // Add subject if exists
        const subject = document.getElementById('subject');
        if (subject) {
            formData.append('subject', subject.value);
        }
        
        // Add newsletter preference (backend expects "true" or "false" string)
        const newsletter = document.getElementById('newsletter');
        if (newsletter) {
            formData.append('newsletter', newsletter.checked ? 'true' : 'false');
        }
        
        // Disable submit button
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalHTML = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = currentLang === 'fr' ? 'Envoi en cours...' : 'Sending...';
        
        // Hide previous messages
        if (messageDiv) {
            messageDiv.style.display = 'none';
            messageDiv.className = 'form-message';
        }
        
        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                body: formData
            });
            
            // Check if response is ok
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.success) {
                if (messageDiv) {
                    messageDiv.textContent = data.message;
                    messageDiv.className = 'form-message success';
                    messageDiv.style.display = 'block';
                }
                form.reset();
            } else {
                if (messageDiv) {
                    messageDiv.textContent = data.message || (currentLang === 'fr' ? 'Une erreur est survenue.' : 'An error occurred.');
                    messageDiv.className = 'form-message error';
                    messageDiv.style.display = 'block';
                }
            }
        } catch (error) {
            console.error('Contact form error:', error);
            if (messageDiv) {
                messageDiv.textContent = currentLang === 'fr' 
                    ? 'Erreur de connexion. Veuillez réessayer plus tard ou contacter directement janmidi@gmail.com' 
                    : 'Connection error. Please try again later or contact directly janmidi@gmail.com';
                messageDiv.className = 'form-message error';
                messageDiv.style.display = 'block';
            }
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalHTML;
        }
    });
}

// ================================
// Video Player
// ================================

// Video quality settings (CSS filter-based simulation)
const videoQualitySettings = {
    high: { filter: 'none', label: { fr: 'Haute', en: 'High' } },
    medium: { filter: 'blur(0.5px)', label: { fr: 'Moyenne', en: 'Medium' } },
    low: { filter: 'blur(1px) contrast(0.95)', label: { fr: 'Basse', en: 'Low' } }
};

let currentVideoQuality = localStorage.getItem('videoQuality') || 'medium';

function setupVideoPlayer() {
    const video = document.getElementById('demo-video');
    const overlay = document.querySelector('.video-overlay');
    
    // Setup quality selector for all video containers
    setupVideoQualitySelectors();
    
    if (!video) return;
    
    // Gestion des erreurs de chargement vidéo
    video.addEventListener('error', (e) => {
        console.error('Video error:', video.error);
        if (video.error) {
            const errorMsg = video.error.message || 'Erreur de chargement de la vidéo';
            console.error('Video error details:', {
                code: video.error.code,
                message: errorMsg
            });
        }
    });
    
    // Gestion du chargement
    video.addEventListener('loadstart', () => {
        console.log('Video loading started');
    });
    
    video.addEventListener('canplay', () => {
        console.log('Video can play');
    });
    
    video.addEventListener('stalled', () => {
        console.warn('Video stalled - network issue');
    });
    
    video.addEventListener('waiting', () => {
        console.log('Video waiting for data');
    });
    
    // Ne pas précharger automatiquement - laisser l'utilisateur décider
    // Preload only when user interacts
    video.addEventListener('click', () => {
        if (video.readyState === 0) {
            video.load();
        }
    }, { once: true });
    
    // Handle play event
    video.addEventListener('play', () => {
        if (overlay) overlay.style.display = 'none';
    });
    
    video.addEventListener('pause', () => {
        if (overlay) overlay.style.display = 'flex';
    });
    
    // Setup all videos on the page
    document.querySelectorAll('video').forEach(v => {
        if (v !== video) {
            v.addEventListener('error', (e) => {
                console.error('Video error:', v.error);
            });
            
            v.addEventListener('click', () => {
                if (v.readyState === 0) {
                    v.load();
                }
            }, { once: true });
        }
    });
    
    // Apply initial quality setting
    applyVideoQuality(currentVideoQuality);
}

function setupVideoQualitySelectors() {
    // Find the first video section to add the global quality selector
    const videoSection = document.querySelector('.video-section');
    if (!videoSection) return;
    
    // Check if selector already exists
    if (document.querySelector('.video-quality-selector')) return;
    
    // Create quality selector
    const selectorContainer = document.createElement('div');
    selectorContainer.className = 'video-quality-selector';
    selectorContainer.innerHTML = `
        <label data-fr="Qualité vidéo :" data-en="Video quality:">Qualité vidéo :</label>
        <select id="video-quality-select">
            <option value="high" data-fr="Haute" data-en="High">Haute</option>
            <option value="medium" data-fr="Moyenne" data-en="Medium" selected>Moyenne</option>
            <option value="low" data-fr="Basse" data-en="Low">Basse</option>
        </select>
    `;
    
    // Insert at the beginning of the section
    const sectionHeader = videoSection.querySelector('.section-header');
    if (sectionHeader) {
        sectionHeader.appendChild(selectorContainer);
    }
    
    // Setup event listener
    const select = document.getElementById('video-quality-select');
    if (select) {
        select.value = currentVideoQuality;
        select.addEventListener('change', (e) => {
            currentVideoQuality = e.target.value;
            localStorage.setItem('videoQuality', currentVideoQuality);
            applyVideoQuality(currentVideoQuality);
        });
    }
    
    // Update language for selector
    setLanguage(currentLang);
}

function applyVideoQuality(quality) {
    const settings = videoQualitySettings[quality] || videoQualitySettings.medium;
    document.querySelectorAll('video').forEach(video => {
        video.style.filter = settings.filter;
    });
}

// ================================
// Lightbox
// ================================

function openLightbox(src) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    
    if (!lightbox || !lightboxImg) return;
    
    lightboxImg.src = src;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    
    if (!lightbox) return;
    
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

// Close lightbox on escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeLightbox();
    }
});

// Close lightbox on background click
document.addEventListener('click', (e) => {
    const lightbox = document.getElementById('lightbox');
    if (e.target === lightbox) {
        closeLightbox();
    }
});

// ================================
// Smooth Scroll
// ================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ================================
// Animation on Scroll
// ================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card, .gallery-item, .spec-card, .usecase-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    observer.observe(el);
});

// Add CSS for animation
const style = document.createElement('style');
style.textContent = `
    .animate-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
`;
document.head.appendChild(style);
