function Pindex = RankSelection(UkPop)
    % Rank selection langsung dari ranking 1..UkPop.
    
    % Probabilitas berdasarkan ranking dari terbaik (1) sampai terburuk (UkPop)
    ranks = UkPop:-1:1;  
    total = sum(ranks);

    r = rand * total;
    cum = 0;

    for i = 1:UkPop
        cum = cum + ranks(i);
        if cum >= r
            Pindex = i;
            return;
        end
    end
end
