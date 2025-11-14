
	
	
	
	
	// function config_get
	function config_get() {
		
		$.ajax({
			type: $( 'form#mail_form' ).attr( 'method' ),
			url: $( 'form#mail_form' ).attr( 'action' ),
			cache: false,
			dataType: 'text',
			data: 'config_get=true',
			
			success: function( res ) {
				if ( res !== '' ) {
					confirm_window = Number( res );
				} else {
					window.alert( '設定ファイルの読み込みに失敗しました。' );
				}
			},
			
			error: function( res ) {
				window.alert( '設定ファイルの読み込みに失敗しました。\nページの再読み込みをしてからもう一度お試しください。' );
			}
		});
		
	}