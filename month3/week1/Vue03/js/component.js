Vue.component('link-list',{
    data:function () {
      return{
          style_ul:{
              width:'100%',
              listStyle:'none',
              zIndex:'1',
              boxShadow:'0 10px 50px rgb(220,193,193)',
              textAlign:'center',
              position:'absolute',
              left:'0',
              top:'26px',
              display:'none'
          },
          style_a:{
              fontSize:'14px',
              padding:'10px 0',
              color:'black',
              display:'block'
          },
          show:false
      }
    },
    props:['datalist','style_out','title'],
   template:`<a href="#" :style="style_out" @mouseenter="enter" @mouseleave="leave">
                    {{title}}
                    
                    <ul :style="style_ul">
                    <li style="height: 4px"></li>
                        <li v-for="item in datalist">
                            <a href="#"  :style="style_a" >{{item}}</a>
                        </li>
                    </ul>
              </a>`,
    methods:{
        enter:function (event) {
            let b = 610;
            //获取移动的总偏移量
            let t = -$(event.target).index()*120;
            // let l = $(event.target).offset().left;
            // l=l-751.5+"px";
            // console.log(l);
            $('.lantiao').stop().animate({right:(b+t)+"px"},200);
            let h = $(event.target).innerHeight();
            // console.log(h);
            this.style_ul.top = h+"px";
            if(!this.show){
                let obj = this;
                this.timer = setTimeout(function () {
                 $(event.target).find('ul').css({
                     display:'block'
                 }).slideDown(50,function () {obj.show=true});

                },10);
            }
           },
        leave:function (event) {
            $('.lantiao').stop().animate({right:'610px'});
            if(this.show){
                let obj = this;
                $(event.target).find('ul').css({
                display:"none"
            }).slideUp(50,function () {
                obj.show=false
            });}

        }
    }
});