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

    /* === CUSTOM CURSOR === */
    const cursor = document.querySelector('.custom-cursor');
    const follower = document.querySelector('.custom-cursor-follower');
    let mouseX = 0, mouseY = 0, followerX = 0, followerY = 0;
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX; mouseY = e.clientY;
        if (cursor) { cursor.style.left = mouseX + 'px'; cursor.style.top = mouseY + 'px'; }
    });
    function animateFollower() {
        followerX += (mouseX - followerX) * 0.15;
        followerY += (mouseY - followerY) * 0.15;
        if (follower) { follower.style.left = followerX + 'px'; follower.style.top = followerY + 'px'; }
        requestAnimationFrame(animateFollower);
    }
    animateFollower();

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

    /* === HEADER SCROLL SHRINK === */
    window.addEventListener('scroll', () => {
        if (header) {
            if (window.scrollY > 100) header.classList.add('scrolled');
            else header.classList.remove('scrolled');
        }
        // Scroll progress bar
        const winScroll = document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        const progressBar = document.querySelector('.scroll-progress-bar');
        if (progressBar) progressBar.style.height = scrolled + '%';
    });

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
