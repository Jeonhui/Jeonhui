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

## Next Steps for Apps Distributed in Texas  

###### November 4, 2025  
<div class="article-text"><p>Today we’re releasing more details about the tools we’re making available for developers to help them meet their compliance obligations under upcoming U.S. state laws, including SB2420 in Texas. While we’re providing these tools to help developers navigate the evolving legal landscape, Apple remains concerned about the potential implications of laws like SB2420 in Texas. Specifically, we worry they could undermine the privacy of all users by requiring the collection of sensitive personal information just to download an app – even those that simply provide weather forecasts or sports scores.</p><p>Starting January 1, 2026, new Apple Accounts in Texas will be subject to new requirements. This includes age assurance and parent or guardian consent on behalf of minors under the age of 18 for downloads, purchases, and significant changes associated with an app. Parents or guardians will also be able to revoke their consent for any app they previously approved.</p><p>To meet their obligations under the law, developers may need to adopt new capabilities to receive age category information, trigger consent for a significant change, and learn when a parent or guardian revokes their approval for a child or teen to use their app. Developers can use the following APIs available in the beta versions of iOS26.2 and iPadOS26.2 to help them meet their obligations. Sandbox testing is also available to help test the user experience when implementing these APIs to comply with Texas state law.</p><h3>Age category information</h3><p>Developers can use the updated <a href="https://developer.apple.com/documentation/declaredagerange/">Declared Age Range API</a> to obtain a user’s age category, which is defined by Texas state law as under 13, 13-15, 16-17, or over 18. Age categories for users with new Apple Accounts in Texas as of January 1, 2026, will be shared with a developer’s app when they request it. The API will also return a signal from the user’s device about the method of age assurance, such as credit card or government ID, and if consent is required when there’s a significant change to an app.</p><h3>Obtaining consent for significant changes</h3><p>Certain types of changes to an app may be considered significant changes under age assurance laws, such as Texas SB2420. It’s the developer’s responsibility to determine when there’s a significant change to their app.</p><p>When a developer determines they have made a significant change to their app, they’ll need to use the <a href="https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic">Significant Change API</a> under the PermissionKit framework to ask the parent or guardian to provide consent for the child or teen to continue using the app or new feature within the app. When the API is called, the child or teen user will see a system dialog to request parental consent and developers can restrict access until consent is obtained.</p><p>Texas state law considers a change in the age rating of an app to be a significant change, and developers should keep their age rating selections current in App Store Connect. When a developer updates their app’s age rating, the rating is updated on all user devices once the version is live. Developers can use a <a href="https://developer.apple.com/documentation/storekit/appstore/ageRatingCode">new property</a> type in StoreKit to automatically check when their app’s age rating has changed on a user’s device and then use the Significant Change API to request parental consent.</p><h3>App consent revocation</h3><p>A parent or guardian in Texas can withdraw consent for any app, which will block launching of the app on the child or teen’s device. The App Store will provide a server notification that developers can configure to <a href="https://developer.apple.com/documentation/appstoreservernotifications/notificationtype">receive notifications</a> that the parent or guardian has withdrawn consent for their app on a child or teen’s device.</p><h3>Sandbox testing</h3><p><a href="https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox">Sandbox testing</a> is now available for the Declared Age Range API and Significant Change API in the beta versions of iOS26.2 and iPadOS26.2.</p><h3>Next steps</h3><ol>
<li>Review documentation and implement the following:</li>
</ol><ul>
<li><a href="https://developer.apple.com/documentation/declaredagerange/">Declared Age Range API</a></li>
<li><a href="https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic">Significant Change API under PermissionKit</a></li>
<li><a href="https://developer.apple.com/documentation/storekit/appstore/ageRatingCode">New age rating property type in StoreKit</a></li>
<li><a href="https://developer.apple.com/documentation/appstoreservernotifications/notificationtype">App Store server notification</a></li>
</ul><ol start="2">
<li>Use Apple’s sandbox testing environment to validate that the APIs have been implemented correctly.</li>
<li>When the Release Candidates of iOS26.2 and iPadOS26.2 become available, submit your apps to App Store Connect so users can update their devices with your updated apps with the customer releases.</li>
<li>Stay tuned for additional communication about future tools to help developers meet upcoming legal obligations in Utah, Louisiana, and Brazil.</li>
</ol></div>  
