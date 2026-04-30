import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },  // montée à 10 users
    { duration: '1m',  target: 10 },  // maintien 10 users
    { duration: '30s', target: 50 },  // montée à 50 users
    { duration: '1m',  target: 50 },  // maintien 50 users
    { duration: '30s', target: 0  },  // descente
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% des requetes < 500ms
    http_req_failed: ['rate<0.01'],   // moins de 1% d'erreurs
  },
};

const BASE_URL = 'http://20.87.90.91';

export default function () {
  // Test route principale
  let res = http.get(`${BASE_URL}/`);
  check(res, {
    'status 200': (r) => r.status === 200,
    'response time OK': (r) => r.timings.duration < 500,
  });

  sleep(1);

  // Test health check
  let health = http.get(`${BASE_URL}/health`);
  check(health, {
    'health OK': (r) => r.status === 200,
  });

  sleep(1);
}
