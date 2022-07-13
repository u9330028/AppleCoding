# HTTP Error Code

# 400 : Bad Request 잘못된 요청
# 401 : Unauthorized(인증이 요구되는 리소스에 접근했을 때 인증하지 않은 상태)
# 403 : Forbiddend(인증된 사용자가 권한이 필요한 리소스에 접근할 수 없을 때 )
# 404 : Not found(요구한 리소스가 없을 때)
# 405 : Method Not Allowed(GET, POST으로 리소스를 요청하고 웹프로그램이 접근허용하지 않을 때)

# 500 : Internal Server Error(웹 프로그램의 내부 오류로 인해서 응답할 수 없을 때)
# 501 : Not implemented(브라우저가 요청한 기능이 웹프로그램에서 구현되지 않을 때)
# 502 : Bad Gateway(웹프로그램이 외부 서비스와 연동하면서 오류가 발생했을 때)
# 503 : Service Unavailable( 웹프로그램의 기능구현은 되어 있는데 서비스 사용이 불가능할 때)

# route데코레이터와 같은 동작을 하는 errorhandler 데코레이터
# @app.errorhandler(404)
# def page_not_found(e):
#       return render_template('404.html'), 404

# abort : Flask에서 에러를 발생 시키는 객체
# abort(404)
