class PB{
    //disX(disY):图片水平(竖直)方向间距,col_num:列数
    constructor(disX,disY,col_num){
        this.x = disX;
        this.y = disY;
        this.col_num = col_num;
        //存储每一列的列宽
        this.w = ($('.pb').width()-(col_num-1)*this.x)/this.col_num;
        //存储每一列具体的初始信息
        this.cols = this.get_col_condition()
    }
    //定义函数获取每一列的横向坐标
    get_col_condition(){
        let cols = [];
        for (let i=0; i< this.col_num;i++){
            let obj = {'h':0,'x':(this.w+this.x)*i};
            cols.push(obj);
        }
        return cols;
    }
    //定义一个函数完成瀑布流的初始装载过程
    first_load_pb(){
        //定义变量存储瀑布流对象
        let pb = this;
        let i = 0;
        let timer = setInterval(function () {
            //向网页中插入一张图片
            //创建img对象,基于js中Image类创建
            let img = new Image();
            img.src = `img/${i+1}.jpg`;
            //为img对象关联onload事件用来监听图片是否加载完成
            img.onload = function () {
                //获取高度最小的列
                let min = pb.get_min_col();
                //将图片插入列.pb标签中
                $('.pb').append(img);
                //修改插入的图片的css样式
                $(img).css({
                    width:`${pb.w}px`,
                    position:"absolute",
                    left:`${min.x}px`,
                    top:`${min.h}px`
                });
                //修改高度最小的这一列的高度值
                //indexOf方法返回某个指定的字符串出现的位置
                let index = pb.cols.indexOf(min);
                pb.cols[index].h = min.h+$(img).height()+pb.y;
            };
            if(++i>=20){
                clearInterval(timer)
            }

        },100)
    }
    //定义一个函数获取瀑布流中高度最小的列
    get_min_col(){
        let min = this.cols[0];
        for(let i=1;i<this.col_num;i++){
            if(min.h >this.cols[i].h){
                min = this.cols[i];
            }
        }
        return min;
    }
    //定义函数完成瀑布流图片位置的重置
    reload_pb(disX,disY,col_cun){
        this.x = disX;
        this.y = disY;
        this.col_num = col_cun;

        // 存储每一列的列宽
        this.w = ($('.pb').width()-(col_num-1)*this.x)/this.col_num;
        // 存储每一列具体的初始信息
        this.cols = this.get_col_condition();
        //将每一列图片的宽度重新调整和列宽一样的宽度
        $('.pb img').css({
            width:`${this.w}px`
        });
        //设置计时器完成每一个图片位置的更新
        let i =0;
        //存储瀑布流对象
        let pb =this;
        let timer = setInterval(function () {
            //获取一张图片对象,eq(index):jQuery对象方法,用来获取指定位置的DOM
            //元素和get(index)作用相同,只不过eq(index)返回一个jQuery对象
            let img = $('.pb img').eq(i);
            //获取当前新的列中最小的高度列
            let min = pb.get_min_col();
            //修改图片的left和top
            img.css({
                left:`${min.x}px`,
                top:`${min.h}px`
            });
            //修改对应列的高度
            let index = pb.cols.indexOf(min);
            pb.cols[index].h = min.h+$(img).height()+pb.y;
            i++;
            if(i>=20){
                clearInterval(timer);
            }
        },10);
    }

}