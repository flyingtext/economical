// Notifications page client-side logic

document.addEventListener('DOMContentLoaded', () => {
  const tabs = document.querySelectorAll('#notification-tabs .tab-link');
  const lists = document.querySelectorAll('.notification-list');
  const loading = document.getElementById('loading');
  const empty = document.getElementById('empty');
  const error = document.getElementById('error');
  const markAllBtn = document.getElementById('mark-all-read');

  function showTab(id) {
    lists.forEach(list => list.classList.add('hidden'));
    const active = document.getElementById(id);
    if (active) active.classList.remove('hidden');
    tabs.forEach(t => t.classList.remove('border-blue-500', 'text-blue-600'));
    const current = document.querySelector(`.tab-link[data-tab="${id}"]`);
    if (current) current.classList.add('border-blue-500', 'text-blue-600');
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', () => showTab(tab.dataset.tab));
  });
  showTab('realtime');

  function updateEmpty() {
    const total = Array.from(lists).reduce((sum, l) => sum + l.children.length, 0);
    if (total === 0) {
      empty.classList.remove('hidden');
    } else {
      empty.classList.add('hidden');
    }
  }

  if (markAllBtn) {
    markAllBtn.addEventListener('click', () => {
      document.querySelectorAll('.notification-list li.unread').forEach(li => {
        li.classList.remove('bg-blue-50', 'font-semibold', 'unread');
        li.classList.add('text-gray-500');
        const indicator = li.querySelector('.unread-indicator');
        if (indicator) indicator.remove();
        li.dataset.read = 'true';
      });
    });
  }

  let opened = false;
  const wsUrl = (location.protocol === 'https:' ? 'wss://' : 'ws://') + location.host + '/ws/notifications';
  try {
    const ws = new WebSocket(wsUrl);
    ws.addEventListener('open', () => {
      opened = true;
      loading.classList.add('hidden');
      updateEmpty();
    });
    ws.addEventListener('message', e => {
      const data = JSON.parse(e.data);
      const channel = data.channel || 'realtime';
      const list = document.getElementById(channel);
      if (!list) return;
      const li = document.createElement('li');
      li.className = 'flex justify-between items-center p-4 hover:bg-gray-50 bg-blue-50 font-semibold unread';
      li.dataset.read = 'false';
      li.innerHTML = `<span>${data.message}</span><span class="unread-indicator ml-4 h-2 w-2 rounded-full bg-blue-500"></span>`;
      list.prepend(li);
      updateEmpty();
    });
    ws.addEventListener('close', () => {
      if (!opened) {
        loading.classList.add('hidden');
        error.classList.remove('hidden');
      }
    });
    ws.addEventListener('error', () => {
      loading.classList.add('hidden');
      error.classList.remove('hidden');
    });
  } catch (err) {
    loading.classList.add('hidden');
    error.classList.remove('hidden');
  }

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/js/sw.js').catch(() => {});
  }
});
