function joinedLogger(level, sep) {
    return function f(...args){
        let arr = [];
        args.forEach((msg) => {
             if (msg.level >= level) {
                 arr.push(msg.text);
             }
         });
         return arr.join(sep)
    };
 }