// Client-side logic for dashboard catalog page

document.addEventListener('DOMContentLoaded', () => {
  const listEl = document.getElementById('dashboard-list');
  if (!listEl) return;

  fetch('/api/dashboards')
    .then(r => r.json())
    .then(dashboards => {
      dashboards.forEach(d => {
        const card = document.createElement('div');
        card.className = 'border rounded p-4 hover:bg-gray-50';
        card.innerHTML = `<h3 class="font-semibold">${d.name}</h3><p>${d.description}</p>`;
        listEl.appendChild(card);

        const wsUrl = `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws/dashboards?dashboard_id=${d.id}`;
        try {
          const ws = new WebSocket(wsUrl);
          ws.addEventListener('message', e => {
            const data = JSON.parse(e.data);
            console.log('dashboard update', d.id, data);
          });
        } catch (err) {
          console.error('WebSocket error', err);
        }
      });
    })
    .catch(err => console.error('Failed to load dashboards', err));
});
