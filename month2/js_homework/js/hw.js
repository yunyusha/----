window.onload = function (ev) {
   // 第一题
   //  let k = prompt('请输入信息','0');
    // k = parseInt(k);
    //     let k100 = k/100;
    //     k100 = parseInt(k100);
    //     let k_50 = k-k100*100;
    //     let k50 = k_50/50;
    //     k50 = parseInt(k50);
    //     let k_10 = k_50 - k50*50;
    //     let k10 = k_10/10;
    //     k10 = parseInt(k10);
    //     let k_5 = k_10 - k10*10;
    //     let k5 = k_5/5;
    //     k5 = parseInt(k5);
    //     let k_1 = k_5 - k5*5;
    //     console.log(k100);
    //     console.log(k50);
    //     console.log(k10);
    //     console.log(k5);
    //     console.log(k_1);

    //第三题
    // let num1 = parseInt(prompt('num1'));
    // let num2 = parseInt(prompt('num2'));
    // let num3 = num1+num2;
    // console.log((num3));
    // num3 = num1 - num2;
    // console.log((num3));
    // num3 = num1*num2;
    // console.log((num3));
    // num3 = num1/num2;
    // console.log((num3));

//    第六题
//     let num1 = 3;
//     let num2 = 4;
//     num1 = num1^num2;
//     num2 = num1^ num2;
//     num1 = num1^num2;
//     console.log(num1+""+num2)

//    第七题

    // let k = parseInt(prompt());
    // if (k%2==0){
    //     console.log(k+"为偶数")
    // }else{
    //     console.log(k+"为奇数")
    // }

//    第八题
//     let k = parseInt(prompt());
//     if ((k%4==0 && k%100!=0)||k%400==0){
//         console.log("闰年")
//     }else{
//         console.log("非闰年")
//     }

//    第九题
//     let num1 = parseInt(prompt('num1'));
//     let num2 = parseInt(prompt('num2'));
//     if (num1>num2){
//         console.log(num1);
//     }else{
//         console.log(num2);
//     }

//    第十题
//     let k = parseInt(prompt())%12;
//
//     if(k==0){
//         console.log("属猴");
//     }else if(k==1){
//         console.log("属鸡");
//     }else if(k==2){
//         console.log("属狗");
//     }else if(k==3){
//         console.log("属猪");
//     }else if(k==4){
//         console.log("属鼠");
//     }else if(k==5){
//         console.log("属牛");
//     }else if(k==6){
//         console.log("属虎");
//     }else if(k==7){
//         console.log("属兔");
//     }else if(k==8){
//         console.log("属龙");
//     }else if(k==9){
//         console.log("属蛇");
//
//     }else if(k==10){
//         console.log("属马");
//
//     }else if(k==11){
//         console.log("属羊");
//     }

//    第十一题
//     for(let i=1;i<=100;i++){
//         if (i==7 ||parseInt(i/10)==7 ||i%7==0||i-parseInt(i/10)*10==7){
//             console.log(i)
//         }
//     }
//    第十二题
//     let num1 = parseInt(prompt('num1'));
//     let num2 = parseInt(prompt('num2'));
//     if (num1>num2){
//         // console.log(num1);
//     }else{
//         let x = num1;
//         num1 = num2;
//         num2 = x;
//     }
//     while (num1%num2!=0){
//         let temp = num1%num2;
//         num1 = num2;
//         num2 = temp;
//     }
//     console.log(num2)

//    第十五题
//     let arr1 = [];
//     let sum =0;
//     for (let i=0;i<10;i++){
//         let k = Math.floor((Math.random()*6)+10);
//         sum = sum +k;
//         arr1.push(k);
//     }
//     console.log(arr1);
//     console.log(sum);

//    第十四题
//     let arr1 = [];
//         for (let i=0;i<15;i++){
//         let k = Math.floor((Math.random()*21)+10);
//         arr1.push(k);
//     }
//         let arr2 = arr1.sort(function (num1,num2) {return num1-num2;  }.reverse);
//        console.log(arr2[14]);

//    第十七题
//     let arr1 =[];
// for(let i=1;i<=4;i++){
//     for(let j=1;j<=4;j++){
//         for(let k =1;k<=4;k++){
//             if (i!=j && i!=k && j!=k){
//                 arr1.push(i+""+j+""+k);
//             }
//         }
//     }
// }
// console.log(arr1);
// console.log(arr1.length);

//    第十九题
    let k = parseInt(prompt());
    let arr1 = [];
    for(let i=0;i<k;i++){
        arr1.push(1);
    }
    console.log(arr1);
     let s = 0;
     let j = 1;
     let arr2=[];
    while (2>1){
        s++;
        j++;

        if (j===3){
            while(arr1[s]==0){
                s++;
                if (s+1==arr1.length){
                    s=0;
                }
            }
            arr1[s]=0;
            arr2.push(s);
            j=1;
        }
        if (s+1==arr1.length){
                s=-1;
            }
        if (arr1.length==arr2.length){
            break;
        }

    }
    console.log(arr2)
};


