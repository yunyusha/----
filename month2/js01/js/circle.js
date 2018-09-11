/*
* for 循环
* for(循环变量初始化;循环条件; 循环变量递增){
*   循环体
* }
*
* for循环的执行流程
* 循环变量初始化-1
* 循环条件-2
* 循环变量递增-3
* 循环体-4
*
* 1->2->4->3->2->4->3->...->2
* */
// 输出1-100的数字
// for(let i = 0;i<100;i=i+2){
//     console.log(i+1)
// }
// 求1-100所有偶数的和
// var sum=0;
// for(let i=0;i<=100;i=i+2){
//     sum=sum+i;
//     document.write((sum)+"<br>");
// }

//求1-100中第一个十位数字含有7的数
// for(let i=1;i<=100;i++){
//     if(i/10==7){
//
//         document.write(i);
//         break;
//     }
// }

// js中将小数转换成整数的操作为
// parseInt()只保留整数部分,不遵循四舍五入
// 强制类型转换,将字符串与小数转换成整数

//求100-999之间所有的水仙花数
for(let i=100;i<1000;i++){
    let b1 = parseInt(i/100);
    let b2 = parseInt((i%100)/10);
    let b3 = i%10;
    if(b1*b1*b1 + b2*b2*b2 + b3*b3*b3 == i){
        document.write(i+"<br>");
    }
}

let arr = [1,2,3,4,5,6,7,8,9,10];
for(let item in arr){
    document.write(arr[item]);
}

//js中for-in经常用来从数组或对象中遍历元素
//js循环具有for循环和while循环两种,for循环用于明确循环次数,
// while循环用于不明确循环次数,但是明确循环条件的循环

/*
* js中的分支结构分为:
* if, if-else, if-else if -else
*
*
* js逻辑运算符:
* &&(并且,等价于python的and),
* ||代表或,等价于or
* ! 逻辑非 ,等价于 not
* */
let num1 = 10;
let result = num1>=5 && num1 <= 20;
document.write(result);