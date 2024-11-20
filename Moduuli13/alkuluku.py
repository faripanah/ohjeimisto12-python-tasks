from flask import Flask

app= Flask(__name__)
@app.route('/alkuluku/<number>')
def alkuluku(number):
    def is_prime(n):
        if n <=1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i ==0 :
                return False
        return True
    vastaus = {
        "Number": number,
        "isPrime": is_prime(number)
    }


    return vastaus



if __name__ == "__main__":
    app.run(use_reloader= True, host='127.0.0.1', port=3000)
