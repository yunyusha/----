//定义一个函数用来获取图片的高度
 function get_img_height() {
    //获取图片对象
    let img = document.querySelector('.con img');
    //获取图片高度
    let h = window.getComputedStyle(img).height;
    //将图片高度应用到.win标签上
    document.querySelector('.win').style.height = h;
 }

 window.onload = function (ev) {
    get_img_height();
    lunbo_pinlv();
 };
//onresize:该事件用来监听浏览器窗口大小是否发生变化
window.onresize = function (ev) {
    get_img_height();
};
//定义函数完成轮播图轮播频率的控制
let num = 0;
//存储当前已经轮播到的是第几张图片
let count = 1;
function lunbo_pinlv() {
    num++;
    if(num >= 100){
        //完成一张图片的轮播
        count++;
        //获取轮播图开始轮播的起始位置
        let con = document.querySelector('.con');
        let b =  parseInt(window.getComputedStyle(con).left);
        //本次轮播的总宽度
        let t = -parseInt(window.getComputedStyle(con).width)/5;
        //本次轮播的总步数
        let s = 20;
        //获取当前轮播的步数
        let c = 0;

        //定义函数完成一张图片的轮播
        let id = 0;
        function lunbo_one_pic() {
            c++;
            con.style.left = (b+(t/s)*c)+"px";
            id = window.requestAnimationFrame(lunbo_one_pic);
            if(c >= s){
                window.cancelAnimationFrame(id);
                if(count >= 5){
                    count = 1;
                    con.style.left = 0;
                }
                change_circle(count);
            }
        }
        //开始轮播
        lunbo_one_pic();
        num = 0;
    }
    window.requestAnimationFrame(lunbo_pinlv);
}
//定义函数完成对span标签class的修改
function change_circle(count) {
    //获取所有的充当圆圈的span标签
    let spans = document.querySelectorAll('.circle span');
    for(let i = 0; i < spans.length; i++){
        spans[i].removeAttribute('class');
    }
    //将第count个图片对应的圆圈置为高亮状态
    spans[count-1].setAttribute('class', 'light');
}
