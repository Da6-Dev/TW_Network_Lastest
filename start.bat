@echo off
chcp 65001 > nul
title Purpur Server Console

:: ====================================================================
:: CONFIGURAÇÕES BÁSICAS
:: ====================================================================
:: Nome exato do arquivo .jar do Purpur na mesma pasta
set "JAR_NAME=purpur.jar"

:: Quantidade de memória RAM (alocar o mesmo valor em Xms e Xmx evita pausas de expansão de heap)
set "RAM=6G"

:: Caminho do Java (use "java" se já estiver no PATH ou aponte para o java.exe desejado, ex: "C:\...\bin\java.exe")
set "JAVA_CMD=java"

:: ====================================================================
:: LOOP DE INICIALIZAÇÃO E AUTO-RESTART
:: ====================================================================
:start
cls
echo ====================================================================
echo  Iniciando Servidor Purpur...
echo  Memoria alocada: %RAM%
echo  JAR: %JAR_NAME%
echo ====================================================================
echo.

"%JAVA_CMD%" -Xms%RAM% -Xmx%RAM% ^
  -XX:+UseG1GC ^
  -XX:+ParallelRefProcEnabled ^
  -XX:MaxGCPauseMillis=200 ^
  -XX:+UnlockExperimentalVMOptions ^
  -XX:+DisableExplicitGC ^
  -XX:+AlwaysPreTouch ^
  -XX:G1NewSizePercent=30 ^
  -XX:G1MaxNewSizePercent=40 ^
  -XX:G1ReservePercent=20 ^
  -XX:G1HeapWastePercent=5 ^
  -XX:G1MixedGCCountTarget=4 ^
  -XX:InitiatingHeapOccupancyPercent=15 ^
  -XX:G1MixedGCLiveThresholdPercent=90 ^
  -XX:G1RSetUpdatingPauseTimePercent=5 ^
  -XX:SurvivorRatio=32 ^
  -XX:+PerfDisableSharedMem ^
  -XX:MaxTenuringThreshold=1 ^
  -Dusing.aikars.flags=https://mcflags.emc.gs ^
  -Daikars.new.flags=true ^
  -Dfile.encoding=UTF-8 ^
  -jar "%JAR_NAME%" --nogui

echo.
echo ====================================================================
echo  Servidor desligado/fechado.
echo  Reiniciando em 10 segundos...
echo  (Pressione CTRL+C para cancelar e fechar este terminal)
echo ====================================================================
timeout /t 10
goto start