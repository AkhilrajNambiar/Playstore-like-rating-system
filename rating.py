from flask import Flask, url_for, render_template,request
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    with open('ratings_so_far.json') as f:
            ratingstore = json.load(f)
    if request.method == 'POST':
        five_stars = int(ratingstore['five_stars'])
        four_stars = int(ratingstore['four_stars'])
        three_stars = int(ratingstore['three_stars'])
        two_stars = int(ratingstore['two_stars'])
        one_star = int(ratingstore['one_star'])
        count = int(ratingstore['count'])
        if 'rating' in request.form:
            content = int(request.form['rating'])
            if content:
                if content == 5:
                    five_stars += 1
                elif content == 4:
                    four_stars += 1
                elif content == 3:
                    three_stars += 1
                elif content == 2:
                    two_stars += 1                    
                elif content == 1:
                    one_star += 1
                count += 1
        ratingstore['five_stars'] = str(five_stars)
        ratingstore['four_stars'] = str(four_stars)
        ratingstore['three_stars'] = str(three_stars)
        ratingstore['two_stars'] = str(two_stars)
        ratingstore['one_star'] = str(one_star)
        ratingstore['count'] = str(count)
        with open('ratings_so_far.json', 'w') as f:
            json.dump(ratingstore, f, indent=2)
    print(ratingstore)
    return render_template('star_rating.html', five_stars=ratingstore['five_stars'], four_stars=ratingstore['four_stars'], three_stars=ratingstore['three_stars'] , two_stars=ratingstore['two_stars'] , one_star=ratingstore['one_star'], count=ratingstore['count'])


if __name__ == "__main__":
    app.run(debug=True)