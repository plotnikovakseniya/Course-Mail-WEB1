def application(env, start_response):
  start_response('200 OK', [('Content-type', 'text/plain')])
  s = env['QUERY_STRING']
  s = s.replace('&', '\r\n')
  return [str.encode(s)]
