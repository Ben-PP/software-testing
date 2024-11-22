import http from 'k6/http'
import { sleep } from 'k6'
export const options = {
  vus: 300,
  duration: '1s',
  thresholds: {
    http_req_duration: ['p(95)<150']
  }
}
export default function () {
  http.get('http://localhost:8000')
  sleep(1)
}
