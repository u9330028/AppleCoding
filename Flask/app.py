from flask import Flask, render_template
import numpy as np

app = Flask(__name__)


@app.route('/user/<userName>')
def getUrlName(userName):
    return 'user : %s' % userName


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/cicle/<float:pi>')
def show_pi(pi):
    return 'Pi %f' % pi


@app.route('/show_html/')
def html():
    return render_template('index.html')


@app.route('/super/<list>')
def displayList(list):
    return render_template('super.html', arrL=list.split(','))


@app.route('/myname/<username>')
def myname(username):
    return render_template('myname.html', name=username)

@app.route('/condition/<FF>')
def def_if(FF):
    return render_template('myname.html', ff=FF)
# ��� �����α׷��� ����ڰ� �� �������� �̿��ؼ� �����α׷��� ������ �ִ� �ڿ�(����,����,��Ÿ)�� ��û�ϸ�
# ���� �� ���ִ� ���·� �簡�� �ϰų�, �ִ� �ڿ��״�� ������������ ��ȯ���ش�.
# �������� ������������� �߻��ϴ� �ڿ� ��ȯ �ܰ迡���� �������� ������ �����̶�� �ܰ踦��ó ����������
# ��ȯ�Ѵ�.

# 1.��������� ����
# 2.������Ʈ ����� ����
# 3.������ ����(1,2�� ȥ�ջ� ����)
# ��������� ����: �������� ���������� ��ȯ�� �������� ���¸� ���� ����
# ������Ʈ(ĳ�ü���) ����� ����: �������� �����ҵ����� ó�����¸� �����ϱ� ���� ù ��° ������ ó����
# ������ ó���� ������Ʈ�� ���� ���� ����


# ���� �ʿ��� HTTP �޽��� ���
# Accept: �ζ������ ó���� �� �ִ� �������� ���� ��ȣ�� text/html
# Accept: Language �ζ������ ������ �� �ִ� �������� ���� ��ȣ��
# Accept: �������� ������ �� �ִ� ��� ���ڵ� ���¿� ��ȣ��
#request / response
if __name__ == "__main__":
    app.run()
