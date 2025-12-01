function Anak = PindahSilang(Bapak,Ibu,JumGen);

TP = 1 + fix(rand*(JumGen-1));

Anak(1,:) = [Bapak(1:TP) Ibu(TP+1:JumGen)];
Anak(2,:) = [Ibu(1:TP) Bapak(TP+1:JumGen)];
