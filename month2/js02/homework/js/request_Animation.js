/*
* requstAnimationFrame(callBack):该方法作用是否告知浏览器在执行下一次
* 页面绘制时须要提前先调用一下callBack.注意每一次调用requestAnimationFrame
* 该方法都会为本次回调函数返回一个唯一的id,次id可以作为取消本次调用的依据
* */


//定义函数用来获取图片的高度
function get_img_height() {
    //获取图片对象
    let img = document.querySelector('.con img');
//    获取图片的高度
    let style_img = window.getComputedStyle(img);
    // console.log(style_img);
    let h = style_img.height;
//    将图片高度应用的.wim标签上面
    document.querySelector('.win').style.height = h;
}
// //获取图片的宽度,w存储图片的宽度
// //定义变量存储浏览器窗口的宽高
// var w = document.documentElement.clientWidth;
// var h = document.documentElement.clientHeight;
window.onload = function (ev) {
    get_img_height();
    lunbo_pinlv();
    bind_click();
};
//onresize: 该事件用来监听浏览器窗口大小是否发生变化
window.onresize = function (ev) {
    // alert("a");
    // clearInterval(timer1);
    get_img_height();
    //获取调整过程中浏览器的宽度和高度
};
//定义函数完成轮播图轮播频率的控制
let num = 0;
     //存储当前已经轮播到的是第几张图片
let count = 1;
//定义变量存储自动轮播对应的id值
let id_auto = 0;
function lunbo_pinlv() {
    num++;
    if (num >= 300){
        //完成一张图片的轮播
        count++;
        //获取轮播图开始轮播的起始位置
        let con = document.querySelector('.con');
        let b = parseInt(window.getComputedStyle(con).left);

        //本次轮播的总宽度
        let t= -parseInt(window.getComputedStyle(con).width)/5;

        //本次轮播的总步数
        let s = 20;
        //获取当前轮播的步数
        let c=0;

        //定义函数完成一张图片的轮播
        let id =0;


        function lunbo_one_pic() {
            c++;
            con.style.left = (b+(t/s)*c)+"px";
            id = window.requestAnimationFrame(lunbo_one_pic);
            if (c>=s){
                window.cancelAnimationFrame(id);
                if(count>=5){
                    count=1;
                    con.style.left = 0;
                }
                change_circle(count);
            }
        }
        //开始轮播
        lunbo_one_pic();
        num=0;

    }
    id_auto = window.requestAnimationFrame(lunbo_pinlv);
}
function change_circle(count) {
    //获取所有的充当圆圈的span标签
    let spans = document.querySelectorAll('.circle span');
    for(let i = 0; i < spans.length; i++){
        spans[i].removeAttribute('class');
    }
    //将第count个图片对应的圆圈置为高亮状态
    spans[count-1].setAttribute('class', 'light');
}

//手动轮播,index:用来记录用户点击的是第几个黑点的下标,
//下标从零开始

function shou_lun(index) {
    //获取手动轮播之前,轮播图所处的位置
    let con = document.querySelector('.con');
    let b = parseInt(window.getComputedStyle(con).left);
    //获取本次轮播总的偏移量
    //获取轮播图轮播之后的位置
    let left = (-parseInt(window.getComputedStyle(con).width)/5)*index;
    //总偏移量计算
    let t = left - b;
    //本次轮播总步数
    let s = 20;
    //当前轮播图所处的位置
    let c = 0;
    //定义计时器完成手动轮播过程
    let timer = setInterval(function () {
        c++;
        con.style.left = (b+(t/s)*c)+"px";
        if (c>=s){
            clearInterval(timer);
            //开启自动轮播
            lunbo_pinlv();
        }
    }, 10);
}
//定义函数完成对四个小圆点的点击事件的绑定
function bind_click() {
    let circles = document.querySelectorAll('.circle span');
    for(let i =0; i<circles.length;i++){
        circles[i].onclick = function () {
            //暂停自动轮播
            window.cancelAnimationFrame(id_auto);
            count = i+1;
            //开启手动轮播
            shou_lun(i);
            //修改指定的小圆点
            change_circle(count);


        }
    }
}




