function huoqu() {
    let img = document.querySelector('img').height;
    console.log(img)
}
window.onload = function (ev) {
    zidong();
};

function zidong() {
    let count=1;
    let a = setInterval(function () {
    count++;
    let width = window.getComputedStyle(document.querySelector('.nei')).width;

    let left = window.getComputedStyle(document.querySelector('.nei')).left;
    let left2 = document.querySelector('.nei');
    // alert(left);
    width = parseInt(width);
    // alert(width);
    //图片
    let h = parseInt(window.getComputedStyle(document.querySelector('img')).width);
    // alert(h);

    let bu = 20;
    let s= 1;
    let x = 0;

    let jishiqi = setInterval(function () {
        s++;
        left = parseInt(left);

            x = left-(h/bu)*s;
            x = x+"px";
            // alert(x);

            console.log(s);
            left2.style.left = x;
            // alert(left2);
        // window.getComputedStyle(document.querySelector('.nei')).left = x;
        if (s>=bu) {
            clearInterval(jishiqi);
            // left2.style.left=0;
            if (count >= 5) {
                left2.style.left = 0;
                count = 1;
            }
        }
    },20)
 },2000)
}
