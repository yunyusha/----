//定义函数用来获取图片高度
function get_img_heigt() {
    //获取图片对象
    let img = document.querySelector('.con img');
//    图片的高度
    let style_img = window.getComputedStyle(img);
    let h = style_img.height;
//    将图片高度应用到.win标签上面
    document.querySelector('.win').style.height = h;

}
//获取图片的宽度,w存储图片的宽度
//定义变量存储浏览器窗口的宽高
var w = document.documentElement.clientHeight;
var h = document.documentElement.clientHeight;

window.onload = function (ev) {
    get_img_heigt();
    autoScroll();
};
var timer1 = null;
function autoScroll() {
    //获取图片宽度
    let w =window.getComputedStyle(document.querySelector('.con img')).width;
    // timer1 控制轮播图轮播的频率
    //用来记录当前轮播的是第几张图片
    let count =1;
    let  timer1 = setInterval(function(){
        count++;
        // 获取con标签
        let con = document.querySelector('.con');
        // 获取轮播图开始轮播的left值
        let b = parseInt(window.getComputedStyle(con).left);
        console.log(window.getComputedStyle(con));
        // 获取本次轮播需要的总偏移量
        let t = -parseInt(w);
        // 定义变量存储本次轮播的总步数
        let s =20;
        // 定义变量存储当前已经执行的步数
        let c = 0;
        // 该计时器控制一张图片的轮播过程
        let timer2 = setInterval(function () {
            c++;
            //移动con标签
            con.style.left = b+(t/s)*c+"px";
            if (c>=s){
                //关闭计时器2
                clearInterval(timer2);
                if(count>=5){
                    con.style.left = 0;
                    count=1;
                }
            }
        }, 10);
    },2000);
}















