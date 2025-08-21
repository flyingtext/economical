// Client-side logic for project catalog page

document.addEventListener('DOMContentLoaded', () => {
  const listEl = document.getElementById('project-list');
  if (!listEl) return;

  fetch('/api/projects')
    .then(r => r.json())
    .then(projects => {
      projects.forEach(p => {
        const card = document.createElement('div');
        card.className = 'border rounded p-4 hover:bg-gray-50';
        card.innerHTML = `<h3 class="font-semibold">${p.name}</h3><p>${p.description}</p>`;
        listEl.appendChild(card);

        const wsUrl = `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws/projects?project_id=${p.id}`;
        try {
          const ws = new WebSocket(wsUrl);
          ws.addEventListener('message', e => {
            const data = JSON.parse(e.data);
            console.log('project update', p.id, data);
          });
        } catch (err) {
          console.error('WebSocket error', err);
        }
      });
    })
    .catch(err => console.error('Failed to load projects', err));
});
