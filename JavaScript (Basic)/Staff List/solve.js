class StaffList {
    constructor(){
        this.members = []
    }
    add(name,age){
       if (age>20){
           this.members.push(name)
       }else if ( age<20 || age==20){
           throw "Error: Staff member age must be greater than 20"
       }
    }
    remove(name){
        if (this.members.includes(name)){
            var index = this.members.indexOf(name);
            this.members.splice(index, 1);
            return true;
        }else{
            return false;
        }
    }
    getSize(){
        return this.members.length;
    }
}