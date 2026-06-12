<!-- ### MySkills
BootStrap & React.js  
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/></a>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/></a>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a>
<img src="https://img.shields.io/badge/React.js-1E8CBE?style=flat-square&logo=JavaScript&logoColor=white"/></a>   -->

<!-- Android & IOS  
<img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=Swift&logoColor=white"/></a> -->
<!-- 
Languages  
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white"/></a>
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=C%2B%2B&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>

algorithms  
<img src="https://img.shields.io/badge/Baekjoon-Gold4-gold?style=flat-square&labelColor=004088"/></a> -->
<!-- 
Contact  
[<img src="https://img.shields.io/badge/l06094@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>](l06094@gmail.com)
<a href="dlwjsgml02@naver.com"><img src="https://img.shields.io/badge/dlwjsgml02@naver.com-0ABF53?style=flat-square&logo=Nintendo&logoColor=white"/></a>
<img src="https://img.shields.io/badge/jeon__hui__22-E4405F?style=flat-square&logo=Instagram&logoColor=white"/></a>  

---
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=6810779s&layout=compact&theme=algolia) 

![Jeonhui's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jeonhui&show_icons=true&theme=algolia)  
 -->

<!-- [![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=whas02)](https://solved.ac/whas02)  

# IOS developer News -->

<!--
 <pre>
    ___  _______   ________  ________   ___  ___  ___  ___  ___     
   |\  \|\  ___ \ |\   __  \|\   ___  \|\  \|\  \|\  \|\  \|\  \    
   \ \  \ \   __/|\ \  \|\  \ \  \\ \  \ \  \\\  \ \  \\\  \ \  \   
 __ \ \  \ \  \_|/_\ \  \\\  \ \  \\ \  \ \   __  \ \  \\\  \ \  \  
|\  \\_\  \ \  \_|\ \ \  \\\  \ \  \\ \  \ \  \ \  \ \  \\\  \ \  \ 
\ \________\ \_______\ \_______\ \__\\ \__\ \__\ \__\ \_______\ \__\
 \|________|\|_______|\|_______|\|__| \|__|\|__|\|__|\|_______|\|__|</pre>
                                                          
                                                                    
-->                                                                    

## Deprecation of the ImageCreator class  

###### June 11, 2026  
<p>As we continue to refine our approach to image generation, the ImageCreator class is being discontinued and will no longer work in iOS 27, iPadOS 27, macOS 27, and visionOS 27 or later. When we introduced the Image Playground framework, we included the ImageCreator class as a way for apps to generate images programmatically using the on-device image generation model.</p><p><strong>If your app uses the ImageCreator class, here's what to expect:</strong></p><ul>
<li><strong>Beta OS releases:</strong> Your code will continue to compile, but you’ll begin to receive warnings in Xcode. Apps using ImageCreator will not function in TestFlight builds and will cause a runtime error.</li>
<li><strong>Public OS releases:</strong> Your code won’t compile, and any features in your app that use ImageCreator won’t work for people using your app.</li>
</ul><p><strong>What you need to do:</strong></p><p>If your app uses ImageCreator, update your implementation before the public release of iOS 27, iPadOS 27, macOS 27, and visionOS 27 to ensure your image generation features continue to work and people using your app won't be affected.</p><ul>
<li><strong>If your app uses ImageCreator:</strong> Transition to presenting the Image Playground sheet, which provides a consistent, system-managed image generation experience. Alternatively, you can integrate another image generation service of your choice.</li>
<li><strong>If you’ve already migrated:</strong> No further action is required.</li>
</ul><p><strong>Resources:</strong></p><p><a href="https://developer.apple.com/documentation/imageplayground">Learn more about the Image Playground framework</a></p><p><a href="https://developer.apple.com/videos/play/wwdc2026/375/">Create high-quality images using Image Playground</a></p>  
