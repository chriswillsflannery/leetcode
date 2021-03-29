// Create a promise from scratch

class MyPromise {
  state = "PENDING";
  value = undefined;
  thenCallbacks = [];
  errorCallbacks = [];

  constructor(callback) {
    callback(this.resolve.bind(this), this.reject.bind(this));
  }

  resolve(value) {
    this.state = "RESOLVED";
    this.value = value;
    this.thenCallbacks.forEach(cb => {
      cb(this.value);
    })
  }

  reject(value) {
    this.state = "REJECTED";
    this.value = value;
    this.errorCallbacks.forEach(cb => {
      cb(this.value);
    });
  }

  then(callback) {
    this.thenCallbacks.push(callback);
    return this;
  }

  catch(callback) {
    this.errorCallbacks.push(callback);
    return this;
  }
}

let promise = new MyPromise((resolve, reject) => {
  setTimeout(() => {
    const rand = Math.ceil(Math.random(1 * 1 + 6) * 6)
    if (rand > 2) {
      resolve("Success")
    } else {
      reject("Error")
    }
  }, 1000);
});

promise
  .then(res => console.log(res))
  .catch(err => console.log(err));