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

## Upcoming expiration of Developer ID Certification Authority (Sub-CA)  

###### October 01, 2026  
<p>The original Developer ID Certification Authority (Sub-CA) expires on February 1, 2027. Certificates issued by this authority will stop working on that date.</p><p>What to do:</p><ol>
<li><strong>Check if you’re affected.</strong> In <a href="https://developer.apple.com/account/resources">Certificates, Identifiers &amp; Profiles</a>, look for certificates expiring on or before February 1, 2027. See <a href="https://developer.apple.com/help/account/certificates/replace-developer-id-certificates">Replacing Developer ID certificates issued from the previous Sub-CA</a> for help identifying your certificate’s authority.</li>
</ol><ol start="2">
<li><strong>Create a new certificate.</strong> Generate a replacement from the current authority, Developer ID Certification Authority (G2). Note: This certificate authority is valid until 2031, but the certificates issued by the certificate authority expire annually and must be renewed each year.</li>
</ol><ul>
<li>If you’re using Xcode 11.4 or earlier, update before creating your new certificate.</li>
<li>When prompted for a Developer ID Certificate Intermediary, select G2 Sub-CA. Choosing another option may issue a certificate that also expires in 2027.</li>
</ul><ol start="3">
<li><strong>Re-sign based on what you distribute.</strong></li>
</ol><ul>
<li>Installer packages (.pkg): Starting February 1, 2027, .pkg files signed with an affected certificate will no longer install. Re-sign all packages with your new certificate before this date.</li>
<li>Mac apps: Previously signed and notarized Mac software (with a secure timestamp) will keep working—no action needed. For future updates, sign with your new certificate and include a secure timestamp for notarization.</li>
</ul>  
