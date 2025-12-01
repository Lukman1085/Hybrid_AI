function x = DekodekanKromosom(Kromosom,Nvar,Nbit,Ra,Rb)

for ii = 1:Nvar,
    x(ii) = 0;
    for jj = 1:Nbit,
        x(ii) = x(ii) + Kromosom((ii-1)*Nbit+jj)*2^(-jj);
    end
    x(ii) = Rb + (Ra - Rb)*x(ii);
end