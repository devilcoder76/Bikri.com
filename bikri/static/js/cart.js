
cart={}

if (localStorage.getItem('cart')!=null){
    cart=JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cartbtn').textContent=`Cart(${Object.keys(cart).length})`
    $('input[name="cart"]').val(localStorage.getItem('cart'));
}

$(document).on('click','.addcart',function(){
    item_id=this.id.toString() 
    cart[item_id]=1
    console.log(cart)
    document.getElementById('cartbtn').textContent=`Cart(${Object.keys(cart).length})`
    data=JSON.stringify(cart);
    localStorage.setItem('cart',data);
    $('input[name="cart"]').val(data);
})

