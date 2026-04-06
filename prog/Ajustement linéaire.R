library(readxl)
library(latex2exp)
df_Lyapounov <- read_excel("C:/Users/maher/OneDrive/Bureau/Documents à rendre/LU3PY122/TP2/df_Lyapounov.xlsx", 
                           col_types = c("numeric", "numeric"))
View(df_Lyapounov)
lm1 = lm(dtheta~t,data=df_Lyapounov)
summary(lm1)
a1=lm1[["coefficients"]][["t"]]
b1=lm1[["coefficients"]][["(Intercept)"]]
tvalues=df_Lyapounov$t
dtheta=df_Lyapounov$dtheta
plot(tvalues,dtheta,type="l",col="blue",
     xlab="t",
     ylab=TeX(r"($log(|\theta_1-\theta_2|)$)"),
     main="Logarithme népérien de la différence entre theta_0=10° et theta_0=9.999°",
     sub=paste("Ajustement: log(|theta_1-theta_2|)=",formatC(a1,format="e",digits=2),"t+",formatC(b1,format="e",digits=2)))
abline(lm1)
