
$(document).on('click','.cartbtncl',function(){
    /*  $ajax({
          type : POST,
          url : "{% url 'products:view_cart' %}",
          data : {
              cart: localStorage.getItem('cart') 
          }
  
      })*/
      console.log('click')
  })

cart={}

if (localStorage.getItem('cart')!=null){
    cart=JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cartbtn').textContent=`Cart(${Object.keys(cart).length})`
}
$(document).on('click','.addcart',function(){
    item_id=this.id.toString() 
    cart[item_id]=1
    console.log(cart)
    document.getElementById('cartbtn').textContent=`Cart(${Object.keys(cart).length})`
    localStorage.setItem('cart',JSON.stringify(cart));
})

