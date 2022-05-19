---
title: Últimos posts
layout: post-index
---
<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <div class="ficha-metadata">
          Escrito por <span class="metadata-input">{{ post.author }}</span> // El <span class="metadata-input">{{ post.date | date_to_string }}</span> en <span class="metadata-input">{{ post.ciudad }}</span>// Clasificado en <span class="metadata-input">morel</span>, <span class="metadata-input">metadatos latinoamericanos</span>, <span class="metadata-input">repositorios</span>.        
      </div>
    </li>
  {% endfor %}
</ul>