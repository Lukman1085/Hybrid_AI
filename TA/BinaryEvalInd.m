function fitness =BinaryEvalInd(FFNNstruk, JumMasukan, JPmasukan, IM,TM);

c = 1.0;
n2 = JumMasukan^2;

Wtemp = FFNNstruk(1:n2);
for ii = 1:JumMasukan
    Wih(ii,:) = Wtemp((ii-1)*JumMasukan+1:ii*JumMasukan);
end

bih = FFNNstruk(n2+1:n2+JumMasukan);
Who = FFNNstruk(n2+JumMasukan+1:n2+2*JumMasukan);
bho = FFNNstruk((JumMasukan+1)^2);

RMSE = 0;
for evaluasi = 1:JPmasukan
    for ii = 1:JumMasukan
        SumWIb = 0;
        for jj = 1:JumMasukan
            SumWIb = SumWIb + (Wih(ii,jj)* IM(evaluasi,jj) + bih(jj));
        end
        Xih(ii) = 1/(1+exp(-c*SumWIb));
    end

    SumWXb = 0;
    for jj = 1:JumMasukan
        SumWXb = SumWXb + (Who(jj) * Xih(jj) + bho);
    end

    Xho = 1/(1+exp(-c*SumWXb));
    RMSE = RMSE + (TM(evaluasi)-Xho)^2;
end

Delta = sqrt(1/JPmasukan * RMSE);
fitness = 1/Delta;