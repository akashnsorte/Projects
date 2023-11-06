*{
    margin: auto;
    padding: 0%;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    box-sizing: border-box;
}

.container{
    width: 100%;
    height: 100vh;
    background-color: rgb(255, 255, 255);
    display: flex;
    align-items: center;
    justify-content: center;
}

.calculator{
    background-color: rgb(207, 45, 45);
padding: 20px;
border-radius: 10px;
}

.calculator form input{
    border: 0;
    outline: 0;
    width: 60px;
    height: 60px;
    border-radius: 10px;
    box-shadow: -8px -8px 15px rgba(255, 255 ,255, 0.1),-8px -8px 15px rgba(255, 255 ,255, 0.1);
    background: transparent;
    font-size: #fff;
    cursor: pointer;
    margin: 10px;
}

form .display{
    display: flex;
    justify-content: flex-end;
    margin: 20px 0;
}
form .display input{
    text-align: right;
    flex: 1;
    font-size: 45px;
    box-shadow: none;
}

form input.equal{
     width: 145px;
}

form input.operator{
    color: chartreuse;
}

body{
    background: black;
}
