var daysUntilMyBirthday = 60;


function birthday() {
    while (daysUntilMyBirthday >= 30) {
        console.log(daysUntilMyBirthday + " Slow down I'm too old.");
        daysUntilMyBirthday--;
    }
    while (daysUntilMyBirthday >= 5) {
        console.log(daysUntilMyBirthday + " Getting Close..");
        daysUntilMyBirthday--;
    }
    while (daysUntilMyBirthday >= 1) {
        console.log(daysUntilMyBirthday + " Yeah BOYEE!! I'm excited");
        daysUntilMyBirthday--;
    }
        console.log("Happy Birthday to me!!!!");
}
birthday();
