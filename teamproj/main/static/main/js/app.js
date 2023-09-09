const tabsBtn = document.querySelectorAll(".tabs_nav-btn");
const tabsItems = document.querySelectorAll(".content_items_2");
const cartabsItems = document.querySelectorAll(".content_items");
const cartabsBtn = document.querySelectorAll(".car_tabs_nav-btn");

tabsBtn.forEach(onTabClick);


function onTabClick(item){
        item.addEventListener("click", function() {
        let currentBtn = item;
        let tabId = currentBtn.getAttribute("data-tab");

        let currentTab = document.querySelector(tabId);


        if( !currentBtn.classList.contains('active')){
            tabsBtn.forEach(function(item) {
                item.classList.remove('active');
            });

            tabsItems.forEach(function(item) {
                item.classList.remove('active');
            });


            currentBtn.classList.add('active');

            currentTab.classList.add('active');
         }
    });
}
document.querySelector('.tabs_nav-btn:nth-child(1)').click();


cartabsBtn.forEach(onCarTabClick);
function onCarTabClick(item){
        item.addEventListener("click", function() {
        let currentBtn = item;
        let tabId = currentBtn.getAttribute("data-tab");

        let currentTab = document.querySelector(tabId);


        if( !currentBtn.classList.contains('active')){
            cartabsBtn.forEach(function(item) {
                item.classList.remove('active');
            });

            cartabsItems.forEach(function(item) {
                item.classList.remove('active');
            });


            currentBtn.classList.add('active');

            currentTab.classList.add('active');
         }
    });
}
document.querySelector('.car_tabs_nav-btn:nth-child(1)').click();