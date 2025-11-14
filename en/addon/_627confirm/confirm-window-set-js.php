<?php

			echo <<<EOM

			
			if ( confirm_window === 2 ) {
				hidden_append( 'confirm_action', 'on' );
				send_setup();
				order_set();
				
				var form_data = new FormData( $( 'form#mail_form' ).get(0) );
				
				$.ajax({
					type: $( 'form#mail_form' ).attr( 'method' ),
					url: $( 'form#mail_form' ).attr( 'action' ),
					cache: false,
					dataType: 'html',
					data: form_data,
					contentType: false,
					processData: false,
					
					success: function( res ) {
						if ( res.indexOf( 'CONFIRM_DELIMITER' ) !== -1 ) {
							var response = res.split( 'CONFIRM_DELIMITER' );
						} else {
							var response = res.split( ',' );
						}
						
						if ( response[0] == 'confirm_success' ) {
EOM;
		
		
		
		
		if ( file_exists( dirname( __FILE__ ) .'/../attachment/attachment-image.js' ) ) {
			include( dirname( __FILE__ ) .'/../attachment/attachment-image.js' );
		}
		
		
		
		
		echo <<<EOM

							if ( $( 'div#confirm_field' ).length ) {
								$( 'input#confirm_action' ).remove();
								$( 'form#mail_form' ).css( 'display', 'none' );
								$( 'div#confirm_window' ).append( response[1] );
								$( 'div#confirm_field' ).fadeIn( 'slow' );
								$( 'html, body' ).animate({
									scrollTop: $( 'div#confirm_field' ).offset().top - scroll_amount
								}, 500 );
							} else {
								window.alert( '確認画面用のHTMLタグが存在しません。' );
							}
						} else {
							response[1] = response[1].replace( /<br>|<br \/>/gi, "\\n" );
							window.alert( response[1] );
						}
						
					},
					
					error: function( res ) {
						window.alert( '通信に失敗しました。\\nページの再読み込みをしてからもう一度お試しください。' );
					}
				});
			}
EOM;
