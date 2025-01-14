// customer section scroll
document.addEventListener('DOMContentLoaded', function () {
    const sliderCust = document.getElementById('slider-cust');
    const leftButton = document.getElementById('left-scroll');
    const rightButton = document.getElementById('right-scroll');
    const slidesCust = Array.from(sliderCust.children);
    const slideWidth = slidesCust[0].offsetWidth;
    const visibleslidesCust = 3;
    let currentIndex = 0;
    // let maxIndex = slidesCust.length - visibleslidesCust;
    let maxIndex = slidesCust.length;

    sliderCust.style.width = `${slideWidth * slidesCust.length}+25px`;

    leftButton.addEventListener('click', function () {
        if (currentIndex > 0) {
            currentIndex--;
            sliderCust.scrollLeft-=(slideWidth + 400)
        }
    });
    
    rightButton.addEventListener('click', function () {
        if (currentIndex < maxIndex) {
            currentIndex++;
            sliderCust.scrollLeft+=(slideWidth + 400)
        }
    });
});

// JavaScript for Smooth Scrolling
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tabs-container ul li');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
