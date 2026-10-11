/* Éléments réutilisables : le « côté Internet » (FAI, DNS public, serveur web) et la box. */
const L = require('./lib');
const { IP } = L;

/* Construit le FAI + un réseau « Internet » (DNS, web). Renvoie rien ; les équipements sont nommés FAI, SW-FAI, DNS-FAI, WWW. */
function internet(sim, h, x0 = 900, y0 = 200) {
  const { dev, link, get } = h;
  dev('inet', 'FAI', x0, y0, 'Internet (FAI)'); dev('sw-8p', 'SW-FAI', x0 + 180, y0); dev('srv-linux', 'DNS-FAI', x0 + 340, y0 - 90, 'DNS public'); dev('srv-linux', 'WWW', x0 + 340, y0 + 100, 'www.exemple.fr');
  link('FAI', 'gi0/1', 'SW-FAI', 'port1'); link('DNS-FAI', 'ens33', 'SW-FAI', 'port2'); link('WWW', 'ens33', 'SW-FAI', 'port3');
  L.cliRun(get('FAI'), 'enable\nconf t\ninterface gi0/0\nip address 203.0.113.1 255.255.255.248\nno shutdown\nexit\ninterface gi0/1\nip address 198.51.100.1 255.255.255.0\nno shutdown\nexit\nip dhcp pool WANPUB\nnetwork 203.0.113.0 255.255.255.248\ndefault-router 203.0.113.1\ndns-server 198.51.100.53\nend');
  L.hostIp(get('DNS-FAI'), '198.51.100.53', '24', '198.51.100.1'); L.hostIp(get('WWW'), '198.51.100.80', '24', '198.51.100.1');
  const s = get('DNS-FAI'); s.dnsd.records = [{ name: 'www.exemple.fr', type: 'A', data: '198.51.100.80' }]; s.dnsd.start();
  const w = get('WWW'); w.httpd.pages['/'] = { type: 'text/html; charset=utf-8', body: '<html><head><title>exemple.fr</title></head><body><h1>Bienvenue sur exemple.fr</h1><p>Si tu lis cette page, ton réseau fonctionne.</p></body></html>', _custom: true }; w.httpd.start();
}
/* Une box branchée au FAI */
function box(sim, h, name = 'BOX', x = 650, y = 200) { const { dev, link } = h; dev('box', name, x, y); link(name, 'wan', 'FAI', 'gi0/0'); }

module.exports = { internet, box };
