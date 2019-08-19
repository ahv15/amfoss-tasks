require 'httparty'
require 'nokogiri'
require'byebug'
link ="https://www.google.com/search?hl=en&source=hp&ei=z51aXf-QO4mHyAOxrpyYAQ&q=linux&oq=linux&gs_l=psy-ab.3..0l3j0i131j0l2j0i131j0l3.889.1881..2079...0.0..0.343.1107.0j5j0j1......0....1..gws-wiz.50viahupFU8&ved=0ahUKEwi_tJqU_47kAhWJA3IKHTEXBxMQ4dUDCAU&uact=5"
unparsed=HTTParty.get(link)
parsed=Nokogiri::HTML(unparsed)
search_results=parsed.css('div.ellip').text
byebug
search_results.each do |search_result|
      puts"search_result"
      end



	
