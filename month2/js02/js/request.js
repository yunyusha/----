 //定义一个函数用来获取图片的高度
 function get_img_height() {
    //获取图片对象
    let img = document.querySelector('.con img');
    //获取图片高度
    let h = window.getComputedStyle(img).height;
    //将图片高度应用到.win标签上
    document.querySelector('.win').style.height = h;

 }

 //定于变量存储浏览器窗口的宽高
 var w = document.documentElement.clientWidth || document.body.clientWidth;
var h = document.documentElement.clientHeight || document.body.clientHeight;

 window.onload = function (ev) {
    get_img_height();
    autoscroll();
 };
//onresize:该事件用来监听浏览器窗口大小是否发生变化
window.onresize = function (ev) {
    get_img_height();
    clearInterval(timer1);
    autoscroll();
};
//定义函数完成轮播图的自动轮播功能
function autoscroll() {
    //获取图片的宽度
    let w = window.getComputedStyle(document.querySelector('.con img')).width;
    //timer1控制轮播图的频率

    //用来记录当前轮播的是第几张图片
    let count = 1;
    //定义一个函数完成一张图片的轮播
    function change_one_pic(width) {
        //获取con标签
        let con = document.querySelector('.con');
        //获取con标签起始的位置
        let left = parseInt(window.getComputedStyle(con).left);
        //获取本次的总偏移量
        let t = -width;
        //获取本次偏移的总步数
        let s = 20;
        //获取当前执行的步数
        let c = 0;
        //定义函数完成本次图片的偏移
        function change_offset() {
            c++;
            con.style.left = (b + (t/s)*c)+"px";
            if (c>=s){
                window.cancelAnimationFrame();
            }
            window.requestAnimationFrame();
        }
        change_offset();
    }
    timer1 = setInterval(
        function () {
            count++;
            //获取con标签
            let con = document.querySelector('.con');
            //获取轮播图的起始left值
            let b = parseInt(window.getComputedStyle(con).left);
            console.log(b);
            //获取本次轮播需要的总偏移量
            let t = -parseInt(w);
            //定义变量存储本次轮播的总步数
            let s = 20;
            //定义变量存储当前已经执行的步数
            let c = 0;
            function change_next_pic() {
                      let timer2 = setInterval(function () {
                c++;
                //移动con标签
                con.style.left = b + ((t/s)*c) + 'px';
                if (c >= s){
                    //关闭计时器2
                    clearInterval(timer2);
                    if (count >= 5){
                        con.style.left = 0;
                        count = 1;

                    }
                    change_circle(count);
                }
            }, 10)
            }
            //该计时器控制一张图片的轮播过程

        }
    ,2000);
}

//定义函数完成对span标签class的修改
 function change_circle(count) {
     //获取所有的充当圆圈的span标签
     let spans = document.querySelectorAll('.circle span');
     for (let i = 0; i < spans.length; i++){
         span[i].removeAttribute('class');
     }
     //将第count个图片对应的圆圈置为高亮状态
     span[count-1].setAttribute('class','light');

 }