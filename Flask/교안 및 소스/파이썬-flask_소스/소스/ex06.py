# jinja2에서 템플릿 표현식

# {% : 템플릿에서의 프로그래밍 영역을 넣기위해 시작하는 기호 -block_start_string 
# %} : 프로그래밍 영역을 기술을 끝내고 프로그래밍 영역을 종료하기 위해 사용하는 기호 - block_end_string 

# {{ : 변수를 출력하기 위해 시작하는 기호 - variable_start_string
# }} : 변수 출력이 끝나고 나서 사용하는 기호 - variable_end_string

# {# : 주석을 넣기 위해 시작하는 기호 - comment_start_string
# #} : 주석을 넣고 종료하기 위해 사용하는 기호 - comment_end_string


from flask import Flask, render_template
app  = Flask(__name__)

@app.route('/')
def temp_test():
    return render_template('temp.html', my_string="템플릿 테스트", my_list=[11,22,33,44,55,66,77])

if __name__ == "__main__":
    app.run(debug=True)
