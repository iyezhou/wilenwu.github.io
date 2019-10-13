{#顶部常驻#}
<div class = "nav">
	//这里把header_nav和a_tag写成同级的，因为后面需要设置隐藏背景色，但是文字显示
	//通过绝对定位让两个重合
     <div class="header_nav">

     </div>
     <div class = "a_tag">
     //把header.swig中相关的a标签粘贴过来
                  <ul id="menu" class="menu">
                       {% for name, path in theme.menu %}
                         {% set itemName = name.toLowerCase() %}
                         <li class="menu-item menu-item-{{ itemName | replace(' ', '-') }}">
                           <a href="{{ url_for(path.split('||')[0]) | trim }}" rel="section">

                             {{ __('menu.' + name) | replace('menu.', '') }}
                           </a>
                         </li>
                       {% endfor %}

                       {% if hasSearch %}
                         <li class="menu-item menu-item-search">
                           {% if theme.swiftype_key %}
                             <a href="javascript:;" class="st-search-show-outputs">
                           {% elseif theme.local_search.enable || theme.algolia_search.enable %}
                             <a href="javascript:;" class="popup-trigger">
                           {% endif %}
                             {% if theme.menu_icons.enable %}
                             {% endif %}
                             {{ __('menu.search') }}
                           </a>
                         </li>
                       {% endif %}
                     </ul>
     </div>

</div>
{#顶部常驻结束#}