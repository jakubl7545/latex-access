JFW Script File                                                           \'  X     autostartevent      latex_access      createobject    &  latex_access       �     nextnonspace           %   %         substring    &   
  # x %     %     stringlength    
  
     %       
  '       %     	      `    process1argcommand    �     %   '     %   %    stringcontains  '  %       
          '          '     %        
        %   %       
    stringleft  '  %     %    stringlength    
  ' 	    %   % 	   nextnonspace    ' 	    %   % 	   getcontents ' 
    % 
   stringlength         
  " �   % 
   isinteger   
  # �%       
  
     %  %  
  %  
  '  %  %  
  % 
 
  '     %  %  
  %  
  '  %  %  
  % 
 
  '  %  %  
  %  
  '        %   % 	        substring    {   
     %  %  
     %   % 	    % 
   stringlength    
       
    stringchopleft  
  '     %  %  
     %   % 	    % 
   stringlength    
       
    stringchopleft  
  '     %  '      %   %    stringcontains  '   �    %     	      �    process2argcommand    �      %   '     %   %    stringcontains  '  %       
          ' 	         ' 	    %        
        %   %       
    stringleft  '  %     %    stringlength    
  ' 
    %   % 
   nextnonspace    ' 
    %   % 
   getcontents '     %   % 
        substring    {   
     % 
    %    stringlength    
       
  ' 
    % 
    %    stringlength    
  ' 
       %   % 
   nextnonspace    ' 
    %   % 
   getcontents '  %   \frac   
  # H%       
  
     %       
     %  %  %  %  %  %    processfraction 
       
  '        %    stringlength         
  # �   %    stringlength         
  
  # %       
  
     %  % 	 
  %  
  % 	 
  %  
  % 	 
  %  
  '     %  % 	 
  %  
  % 	 
  %  
  % 	 
  %  
  % 	 
  %  
  % 	 
  %  
  '           %   % 
        substring    {   
     %  % 	 
     %   % 
    %    stringlength    
       
    stringchopleft  
  '     %  % 	 
     %   % 
    %    stringlength    
       
    stringchopleft  
  '        %  %    stringcontains  '  %  '    �       �    processfromtocommand      �  %   '     %   %    stringcontains  '  %        
        %   %       
    stringleft  '  %     %    stringlength    
  '     %   %    nextnonspace    '  %       
  %  
  '     %   %         substring    _   
     %       
  '     %   %    getcontents '  %    from   
  %  
  '     %   %         substring    {   
     %     %    stringlength    
       
  '     %     %    stringlength    
  '           %   %    nextnonspace    '     %   %         substring    ^   
     %       
  '     %   %    getcontents '  %    to     
  %  
  '     %   %         substring    {   
     %     %    stringlength    
       
  '     %     %    stringlength    
  '        %    of     
  '  %     %   %       
    stringchopleft  
  '  %  '      %  %    stringcontains  '   T    %     	      �    getcontents        %   %         substring    {   
     %       
  '        '  %    ����
  # � %     %     stringlength    
  
        %   %         substring    {   
     %       
  '        %   %         substring    }   
     %       
  '     %       
  '   l    %       
  '     %   %       
  %  %  
       
    substring   '        %   %         substring   '     %     	      �    processmaths       %   '     %    smmreplacesymbolswithmarkup '     %   \int     integral      processfromtocommand          %   \sum     sum   processfromtocommand          %   \lim_    Lim as   then                process1argcommand        %   \sqrt    Begin root   end root     root           process1argcommand        %   ^    Begin super  End super    To the         process1argcommand        %   _            smmgetstartmarkupforattributes           smmgetendmarkupforattributes                process1argcommand        %   \mathbf           smmgetstartmarkupforattributes            smmgetendmarkupforattributes                process1argcommand        %   \mathbb           smmgetstartmarkupforattributes            smmgetendmarkupforattributes                process1argcommand        %   \mbox                         process1argcommand        %   \bar          bar             process1argcommand        %   \overline         bar             process1argcommand        %   \pmod    mod       mod        process1argcommand        %   \frac    Fraction     over     End frac     over           process2argcommand        %   \colvec  vector           smmgetstartmarkupforattributes  
           smmgetendmarkupforattributes             smmgetstartmarkupforattributes  
           smmgetendmarkupforattributes                process2argcommand     %     	      �     sayline      getline '   $  processmaths          %     stringisblank       blank   '         %     processmaths    '         %     
          say            sayline          �    processfraction            %     stringlength         
  # �    %    stringlength         
  
  # �    %               substring    d   
  
  # �    %              substring    d   
  
        %               substring        
     %               substring   
  '      %              substring        
     %              substring   
  '  %     by     
  %  
  '        %     stringlength         
  # D   %    stringlength         
  
  # \%        
 	 
  # t%     	   
  
  # �%       
 	 
  # �%    	   
  
     %        
  '  %      haf&third&quarter&fifth&sixth&seventh&eighth&ninth   &      %    stringtoint      
    stringsegment   
  '  %        
 
    %   s   
  '           %     stringlength         
  # �   %    stringlength         
  
  # �%       
  
     %       
  %   
       
  %  
       
  %  
  '     %       
  %  
       
  %   
       
  %  
       
  %  
       
  %  
  '     %     	      ,    $togglemaths    $  processmaths             &  processmaths             maths to be read as plain latex  Processing off    saymessage             &  processmaths             Maths to be processed to a more verbal form  Processing on     saymessage           �     braillebuildline    $  processmaths            getline '   $  latex_access      %     nemeth  '      %                       brailleaddstring                  	      �     isinteger           '  %     %     stringlength    
        %   %         substring    0   
 	 # �    %   %         substring    9   
  
                	      %       
  '                	      �    $inputmatrix        latex_access_matrix   createobject    &  matrix       &  row      &  column  $  matrix         getselectedtext   tex_init        Initialised     '   %      $  matrix      rows      inttostring 
  '   %     by     
  '   %      $  matrix      columns   inttostring 
  '   %     matrix 
  '      %     saystring         �     $matrixright    $  column  $  matrix      columns 
     $  column       
  &  column     $  matrix    $  row $  column    get_cell      saystring             end row   saystring            �     $matrixleft $  column       
 
    $  column       
  &  column     $  matrix    $  row $  column    get_cell      saystring             start row     saystring            �     $matrixdown $  row $  matrix      rows    
     $  row      
  &  row    $  matrix    $  row $  column    get_cell      saystring             end column    saystring            �     $matrixup   $  row      
 
    $  row      
  &  row    $  matrix    $  row $  column    get_cell      saystring             start columnd     saystring            �     $sayrow    %         
 
 # L %   $  matrix      rows    
  
        $  matrix    %          get_row   saystring             Invalid row   saystring            �     $saycolumn     %         
 
 # P %   $  matrix      columns 
  
        $  matrix    %          get_col   saystring             Invalid column    saystring            P    $preprocessoradd        Enter the custom LaTeX you wish to re-define.    Initial LaTeX   %     inputbox           Enter the definition of the custom command, that is, the standard LaTeX to which it is equivalent.   Translation %    inputbox       $  latex_access      %   %    preprocessor_add          �     $preprocessorcsv        Enter the name of the CSV file you wish to load  Filename    %     inputbox          %     fileexists     $  latex_access      %     load_csv              File not found    saystring            