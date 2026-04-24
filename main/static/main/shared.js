

document.addEventListener('DOMContentLoaded', () => {

    /* === SPLASH SCREEN === */
    const splash = document.getElementById('splash-screen');
    const header = document.querySelector('.header');
    
    if (splash) {
        document.body.style.overflow = 'hidden';
        if (header) header.style.opacity = '0';
        
        window.addEventListener('load', () => {
            setTimeout(() => {
                splash.classList.add('hidden');
                setTimeout(() => {
                    if (header) header.style.opacity = '1';
                    document.body.style.overflow = 'visible';
                }, 800);
            }, 1800);
        });
    } else {
        document.body.style.overflow = 'visible';
        if (header) header.style.opacity = '1';
    }



    /* === SCROLL ANIMATIONS === */
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.classList.contains('staggered')) {
                    const parent = entry.target.parentElement;
                    const siblings = Array.from(parent.querySelectorAll('.staggered'));
                    const index = siblings.indexOf(entry.target);
                    const delayMs = Math.min((index + 1) * 100, 500);
                    entry.target.style.transitionDelay = `${delayMs}ms`;
                    entry.target.classList.add(`delay-${delayMs}`);
                }
                entry.target.classList.add('is-visible');
                if (entry.target.classList.contains('pop-up') && entry.target.querySelector('.count-up')) {
                    const countEl = entry.target.querySelector('.count-up');
                    if (!countEl.classList.contains('counted')) {
                        countEl.classList.add('counted');
                        startCountUp(countEl, parseInt(countEl.getAttribute('data-target')));
                    }
                }
            }
        });
    }, { root: null, rootMargin: '0px', threshold: 0.15 });
    document.querySelectorAll('.animate-on-scroll').forEach(el => scrollObserver.observe(el));

    /* === COUNT UP === */
    function startCountUp(element, target) {
        let current = 0;
        const steps = 60, duration = 2000;
        const increment = target / steps;
        const stepTime = Math.floor(duration / steps);
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) { element.innerText = target + '+'; clearInterval(timer); }
            else { element.innerText = Math.floor(current) + '+'; }
        }, stepTime);
    }

    /* === HEADER SCROLL BEHAVIOR === */
    const updateHeader = () => {
        if (!header) return;
        
        // Detect if we are on a page with a hero that needs transparency
        const hasHero = document.querySelector('.about-hero-video') || 
                        document.querySelector('.hero-banner') || 
                        document.querySelector('.page-hero') ||
                        document.querySelector('.service-hero');

        if (window.scrollY > 100) {
            header.classList.add('scrolled');
            // When scrolled down over content (usually light), use a DARK navbar for contrast
            header.style.background = 'rgba(10, 44, 28, 0.98)'; // Deep brand green
            header.style.backdropFilter = 'blur(15px)';
            header.style.borderBottom = '1px solid rgba(255,255,255,0.1)';
            
            header.querySelectorAll('.nav-links a').forEach(a => {
                a.style.color = 'rgba(255,255,255,0.8)';
                if (a.classList.contains('active')) a.style.color = '#ffffff';
            });
            
            const logoImg = header.querySelector('.logo-icon-img');
            if (logoImg) logoImg.style.filter = 'brightness(0) invert(1)';
            
        } else {
            header.classList.remove('scrolled');
            if (hasHero) {
                // On Hero (transparent mode)
                header.style.background = 'rgba(255,255,255,0.1)';
                header.style.backdropFilter = 'blur(10px)';
                header.style.borderBottom = '1px solid rgba(255,255,255,0.2)';
                header.querySelectorAll('.nav-links a').forEach(a => {
                    a.style.color = a.classList.contains('active') ? '#ffffff' : 'rgba(255,255,255,0.7)';
                });
                const logoImg = header.querySelector('.logo-icon-img');
                if (logoImg) logoImg.style.filter = 'brightness(0) invert(1)';
            } else {
                // Regular light header at top (if no hero)
                header.style.background = 'rgba(255,255,255,0.95)';
                header.style.backdropFilter = 'blur(10px)';
                header.style.borderBottom = '1px solid rgba(0,0,0,0.05)';
                header.querySelectorAll('.nav-links a').forEach(a => {
                    a.style.color = ''; // Use default CSS
                });
                const logoImg = header.querySelector('.logo-icon-img');
                if (logoImg) logoImg.style.filter = '';
            }
        }
        
        // Scroll progress bar
        const winScroll = document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        const progressBar = document.querySelector('.scroll-progress-bar');
        if (progressBar) progressBar.style.height = scrolled + '%';
    };

    window.addEventListener('scroll', updateHeader);
    updateHeader(); // Initial load check

    /* === MAGNETIC BUTTONS === */
    document.querySelectorAll('.magnetic-btn').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const pos = btn.getBoundingClientRect();
            const x = e.clientX - pos.left - pos.width / 2;
            const y = e.clientY - pos.top - pos.height / 2;
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });
        btn.addEventListener('mouseleave', () => { btn.style.transform = 'translate(0,0)'; });
    });

    /* === TILT EFFECT === */
    document.querySelectorAll('.tilt-effect').forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const xRot = 10 * ((e.clientY - rect.top - rect.height / 2) / rect.height);
            const yRot = -10 * ((e.clientX - rect.left - rect.width / 2) / rect.width);
            el.style.transform = `perspective(1000px) rotateX(${xRot}deg) rotateY(${yRot}deg)`;
        });
        el.addEventListener('mouseleave', () => { el.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)'; });
    });

    /* === PARALLAX === */
    document.querySelectorAll('.parallax-wrap').forEach(wrap => {
        const el = wrap.querySelector('.parallax-el');
        if (!el) return;
        wrap.addEventListener('mousemove', (e) => {
            const rect = wrap.getBoundingClientRect();
            const x = (e.clientX - rect.left - rect.width / 2) / (rect.width / 2);
            const y = (e.clientY - rect.top - rect.height / 2) / (rect.height / 2);
            el.style.transform = `scale(1.05) translate(${x * -10}px, ${y * -10}px)`;
        });
        wrap.addEventListener('mouseleave', () => { el.style.transform = 'scale(1)'; });
    });

    /* === PORTFOLIO FILTER === */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.textContent.trim();
            portfolioItems.forEach(item => {
                if (filter === 'All' || item.dataset.category === filter) {
                    item.style.display = 'block';
                    item.style.opacity = '1';
                } else {
                    item.style.opacity = '0';
                    setTimeout(() => { item.style.display = 'none'; }, 300);
                }
            });
        });
    });

});
